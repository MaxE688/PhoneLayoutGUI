"""
TODO:
    - Implement Yealink models


(topsoftkey\d+ \w+: *.* *\d*\n){3,4}\n


"""

import re
from Model.Tile import Tile

class InitTileConfig:
    
    def __init__(self,model, brand, cfg):
   
        self.model = model
        self.brand = brand
        self.cfg = cfg

        self.btnList = []



    def getTiles(self):

        self.topBtnGroup = None
        self.exp40Group = None
        self.btnGroup = None

        if self.brand == "Astra":
            keyStr = "(?P<id>softkey\d+)"
            typeStr = "type: *(?P<type>\w+ *[^\st])"
            lineStr = "line: *(?P<line>\d+)"
            valueStr = "value: *(?P<value>.+)"
            labelStr = "label: *(?P<label>\w+ *\w+)"


            topBtnGroupRegx = re.compile("((topsoftkey\d+ \w+: *.* *\d*\n){3,4})\n")
            btnGroupRegx = re.compile("(((?<=[^p])softkey\d+ \w+: *.* *\d*\n?){1,4})\n*")
            if self.model == "Astra 6737i":
                self.topBtnGroup = topBtnGroupRegx.findall(self.cfg)
            
            self.btnGroup = btnGroupRegx.findall(self.cfg)

        elif self.brand == "Yealink":

            keyStr = "(?P<id>linekey.\d+)"
            typeStr = ".type *= *(?P<type>\w+)"
            lineStr = ".line *= *(?P<line>\w+)"
            valueStr = ".value *= *(?P<value>\w+)"
            labelStr = ".label *= *(?P<label>\w+ *\w*)"

            exp40Group = re.compile("((expansion_module.\d.key.\d+.\w+ *= *.+\n){1,5})\n*") # expansion_module.\d.key.\d+
            btnGroupRegx = re.compile("((linekey.\d+.\w+ *= *.+\n){1,5})\n*")

            self.exp40Group = exp40Group.findall(self.cfg)
            self.btnGroup = btnGroupRegx.findall(self.cfg)



        keyR = re.compile(keyStr)
        typeR = re.compile(typeStr)
        lineR = re.compile(lineStr)
        valueR = re.compile(valueStr)
        labelR = re.compile(labelStr)



        if(self.topBtnGroup != None):
            id = re.compile("(?P<id>topsoftkey\d+)")
            self.parseMatch(self.topBtnGroup, id, typeR, lineR, valueR, labelR)
            self.fillEmptyTopkeys()

        if(self.btnGroup != None):
            id = re.compile(keyR)
            self.parseMatch(self.btnGroup, id, typeR, lineR, valueR, labelR)

        if self.exp40Group != None:
            id = re.compile("(?P<id>expansion_module.\d.key.\d+)")
            self.parseMatch(self.exp40Group, id, typeR, lineR, valueR, labelR)

        return self.btnList


    def parseMatch(self, btnGroups, idR, typeR, lineR, valueR, labelR):

        idNumR = re.compile("\d+")

        pID = 1
        for btnTup in btnGroups:
            btn = btnTup[0]

            id = idR.search(btn)
            type = typeR.search(btn)
            line = lineR.search(btn)
            value = valueR.search(btn)
            label = labelR.search(btn)

            idNum = int(idNumR.search(id['id'])[0])

            print(idNum)
            print()

            # if pID is 2 greater than idNum
            if idNum - pID > 1:
                while idNum - pID >= 1:
                    tempID = id['id'].replace(str(idNum), str(pID))
                    print("ID: " + id['id'])
                    print("temp ID: " + tempID)
                    print('prevID: ' + str(pID))
                    print('idNum: ' + str(idNum))
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
