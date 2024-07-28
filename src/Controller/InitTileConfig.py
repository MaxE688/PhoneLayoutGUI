
import re
from Model.Tile import Tile
from Model.NewConfiguration import NewConfiguration
from Model.constants import Brand, Model

class InitTileConfig:
    """
    Controller responsible for parsing config string, and creating the tiles

    Attributes
    ----------
    model : str
        model of the phone being edited
    brand : str
        brand of the phone being edited
    cfg : str
        Config string entered by user
    btnList : Tile[]
        list of tiles created from cfg string
    topBtnGroup : List
        list of button groups from regex operation
    exp40Group : List
        list of button groups from regex operation
    btnGroup : List
        list of button groups from regex operation
    
    Methods
    -------
    getTiles()
        returns list of tiles generated from config string
    parseMatch(
        btnGroups : List, 
        idR : Pattern[str], 
        typeR : Pattern[str], 
        lineR : Pattern[str], 
        valueR : Pattern[str], 
        labelR : Patter[str]
    )
        parse the config string to build list of tiles
    fillEmptyTopKeys()
        Any top keys not included in config string will be created for phone models that use topsoftkeys
    
    """
    
    def __init__(self,model, brand, cfg):
        """
        Parameters
        ----------
        model : str
            model of phone
        brand : str
            brand of phone
        cfg : str
            config string entered by user
        """
   
        self.model = model
        self.brand = brand

        if(cfg == ""):
            self.cfg = NewConfiguration.getString(model)
            print(self.cfg)
        else:
            self.cfg = cfg

        self.btnList = []



    def getTiles(self):
        """Return list of tiles
        
        Returns a list of type Tile generated from config string entered by user
        """

        self.topBtnGroup = None
        self.exp40Group = None
        self.btnGroup = None

        if self.brand == Brand.AASTRA.value:
            keyStr = r"(?P<id>softkey\d+)"
            typeStr = r"type: *(?P<type>\w+ *[^\st])"
            lineStr = r"line: *(?P<line>\d+)"
            valueStr = r"value: *(?P<value>.+)"
            # labelStr = r"label: *(?P<label>\w+ *\w+)"
            labelStr = r"label: *(?P<label>\w+( *\w*)*)"


            topBtnGroupRegx = re.compile(r"((topsoftkey\d+ \w+: *.* *\d*\n){3,4})\n")
            btnGroupRegx = re.compile(r"(((?<=[^p])softkey\d+ \w+: *.* *\d*\n?){1,4})\n*")
            if self.model == Model.AASTRA_6737.value:
                self.topBtnGroup = topBtnGroupRegx.findall(self.cfg)
            
            self.btnGroup = btnGroupRegx.findall(self.cfg)

        elif self.brand == Brand.YEALINK.value:

            keyStr = r"(?P<id>linekey.\d+)"
            typeStr = r".type *= *(?P<type>\w+)"
            lineStr = r".line *= *(?P<line>\w+)"
            valueStr = r".value *= *(?P<value>\w+)"
            # labelStr = r".label *= *(?P<label>\w+ *\w*)"
            labelStr = r".label *= *(?P<label>\w+( *\w*)*)"

            exp40Group = re.compile(r"((expansion_module.\d.key.\d+.\w+ *= *.+\n){1,5})\n*") # expansion_module.\d.key.\d+
            btnGroupRegx = re.compile(r"((linekey.\d+.\w+ *= *.+\n){1,5})\n*")

            self.exp40Group = exp40Group.findall(self.cfg)
            self.btnGroup = btnGroupRegx.findall(self.cfg)



        keyR = re.compile(keyStr)
        typeR = re.compile(typeStr)
        lineR = re.compile(lineStr)
        valueR = re.compile(valueStr)
        labelR = re.compile(labelStr)



        if(self.topBtnGroup != None):
            id = re.compile(r"(?P<id>topsoftkey\d+)")
            self.parseMatch(self.topBtnGroup, id, typeR, lineR, valueR, labelR)
            self.fillEmptyTopkeys()

        if(self.btnGroup != None):
            id = re.compile(keyR)
            self.parseMatch(self.btnGroup, id, typeR, lineR, valueR, labelR)

        if self.exp40Group != None:
            id = re.compile(r"(?P<id>expansion_module.\d.key.\d+)")
            self.parseMatch(self.exp40Group, id, typeR, lineR, valueR, labelR)

        return self.btnList


    def parseMatch(self, btnGroups, idR, typeR, lineR, valueR, labelR):
        """Uses regex to parse through config string
        
        Uses regex to parse through config string in order to create tiles
        """

        idNumR = re.compile(r"\d+")

        pID = 1
        for btnTup in btnGroups:
            btn = btnTup[0]

            id = idR.search(btn)
            type = typeR.search(btn)
            line = lineR.search(btn)
            value = valueR.search(btn)
            label = labelR.search(btn)

            idNum = int(idNumR.search(id['id'])[0])

            # print("id:", idNum)
            # print()

            # if pID is 2 greater than idNum
            if idNum - pID > 1:
                while idNum - pID >= 1:
                    tempID = id['id'].replace(str(idNum), str(pID))
                    print(r"ID: " + id['id'])
                    print(r"temp ID: " + tempID)
                    print(r'prevID: ' + str(pID))
                    print(r'idNum: ' + str(idNum))
                    print()
                    tempLabel = str(pID)

                    t = Tile(
                                tempID,
                                None,
                                None,
                                None,
                                tempLabel
                    )
                    self.btnList.append(t)
                    pID += 1

            t = Tile(
                        # self.tileFrame,
                        id['id'] if id else None,
                        type['type'] if type else None,
                        line['line'] if line else None,
                        value['value'] if value else None,
                        label['label'] if label else None
                    )
            
            self.btnList.append(t)
            pID += 1
           


    def fillEmptyTopkeys(self):
        """fills list of topkeys with keys that were not included in config string"""

        index = 1
        for i, b in enumerate(self.btnList):
            id = int(b.id[-1])
            if i + 1 == id:
                index = id + 1
                continue
            else:
                for x in range(index, id):
                    t = Tile(
                                'topsoftkey' + str(x),
                                'NA',
                                '1',
                                None,
                                "auto_gen" + str(x + 1)
                            )
                    self.btnList.insert(x-1, t)

        for i in range(len(self.btnList) + 1, 7):
            t = Tile(
                        'topsoftkey' + str(i),
                        'NA',
                        '1',
                        None,
                        "auto_gen2"
                    )
            self.btnList.insert(i, t)

