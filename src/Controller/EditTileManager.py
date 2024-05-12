
import re
from Model.constants import phoneModels
from View.EditTileFrame import EditTileFrame

class EditTileManager:

    def __init__(self, frame, tile):
        self.frame = frame
        self.tfManager = frame.frameManager
        self.tile = tile
        self.model = frame.frameManager.model
        self.brand = phoneModels[self.model]["brand"]
        self.typeOptions = {
                0:"NA",
                1:"Conference",
                2:"Forward",
                3:"Transfer",
                4:"Hold",
                5:"DND",
                7:"Call Return",
                8:"SMS",
                9:"Directed Pickup",
                10:"Call Park",
                11:"DTMF",
                12:"Voice Mail",
                13:"Speed Dial",
                14:"Intercom",
                15:"Line",
                16:"BLF",
                17:"URL",
                18:"Group Listening",
                20:"Private Hold",
                22:"XML Group",
                23:"Group Pickup",
                24:"Multicast Paging",
                25:"Record",
                27:"XML Browser",
                34:"Hot Desking",
                35:"URL Record",
                38:"LDAP",
                39:"BLF List",
                40:"Prefix",
                41:"Zero Touch",
                42:"ACD",
                45:"Local Group",
                46:"Network Group",
                49:"Custom Button",
                50:"Keypad Lock",
                55:"Meet-Me Conference",
                56:"Retrieve Park",
                57:"Hoteling",
                58:"ACD Grace",
                59:"Sisp Code",
                60:"Emergency",
                61:"Directory",
               }
        self.editFrame = EditTileFrame(self)
        self.editFrame.center()
        

    def getTypeOpts(self):
        if self.brand == "Astra":
            return self.astraTypeOptions()
        elif self.brand == "Yealink":
            return self.yealinkTypeOptions()


    def astraTypeOptions(self):
        return self.typeOptions.values()

    def yealinkTypeOptions(self):
        options = []
        for key in self.typeOptions.keys():
            options.append(str(key) + ": " + self.typeOptions[key])
            # options.append(str(self.typeOptions.index(val)) + ": " + val)

        return options

    def getCurrOpt(self):
        print(self.tile.type)
        print(type(self.tile.type))
        if self.brand == "Astra":
            return str(self.tile.type)
        elif self.brand == "Yealink":
            option = str(self.tile.type) + ": "
            if type(self.tile.type) != "int":
                option += str(self.typeOptions[int(self.tile.type)])
            else:
                option += str(self.typeOptions[self.tile.type])
            print()
            print(option)
            print()
            return option

    def updateTile(self, type, line, value, label):
        if self.brand == "Astra":
            self.tile.type = type
        elif self.brand == "Yealink":
            self.tile.type = re.match("\d+", type)[0]
        self.tile.line = line
        self.tile.value = value
        self.tile.label = label
        self.tile.tileText.set(label)



    # def getKey(self, val):
    #      keyList = list(self.typeOptions.keys())
    #      valList = list(self.typeOptions.values())
    #
    #      key = keyList[valList.index(val)]
    #
    #      return key

"""
0-NA
1-Conference
2-Forward
3-Transfer
4-Hold
5-DND
7-Call Return
8-SMS
9-Directed Pickup
10-Call Park
11-DTMF
12-Voice Mail
13-Speed Dial
14-Intercom
15-Line
16-BLF
17-URL
18-Group Listening
20-Private Hold
22-XML Group
23-Group Pickup
24-Multicast Paging
25-Record
27-XML Browser
34-Hot Desking
35-URL Record
38-LDAP
39-BLF List
40-Prefix
41-Zero Touch
42-ACD
45-Local Group
46-Network Group
49-Custom Button
50-Keypad Lock
55-Meet-Me Conference
56-Retrieve Park
57-Hoteling
58-ACD Grace
59-Sisp Code
60-Emergency
61-Directory



 0:"Conference":0,
 1:"Conference":1,
 2:"Forward":2,
 3:"Transfer":3,
 4:"Hold":4,
 5:"DND":5,
 7:"Call Return":7,
 8:"SMS":8,
 9:"Directed Pickup":9,
 10:"Call Park":10,
 11:"DTMF":11,
 12:"Voice Mail":12,
 13:"Speed Dial":13,
 14:"Intercom":14,
 15:"Line":15,
 17:"URL":17,
 16:"BLF":16,
 18:"Group Listening":18,
 20:"Private Hold":20,
 22:"XML Group":22,
 23:"Group Pickup":23,
 24:"Multicast Paging":24,
 25:"Record":25,
 27:"XML Browser":27,
 34:"Hot Desking":34,
 35:"URL Record":35,
 38:"LDAP":38,
 39:"BLF List":39,
 40:"Prefix":40,
 41:"Zero Touch":41,
 42:"ACD":42,
 45:"Local Group":45,
 46:"Network Group":46,
 49:"Custom Button":49,
 50:"Keypad Lock":50,
 55:"Meet-Me Conference":55,
 56:"Retrieve Park":56,
 57:" Hoteling":57,
 58:"ACD Grace":58,
 59:"Sisp Code":59,
 30:"Emergency":60,
 61:"Directory":61,

"""
