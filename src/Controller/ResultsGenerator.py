from Model.constants import Brand, Model, phoneModels

class ResultsGenerator:

    def __init__(self, tileList, model):
        brand = phoneModels[model]["brand"]
        self.strings = ""
        match(brand):
            case Brand.AASTRA.value:
                self.setAastraID(tileList)
                self.strings = self.astra(tileList)
            case Brand.YEALINK.value:
                if model == Model.YEALINK_EXP40.value:
                    self.setEXP40ID(tileList)
                else:
                    self.setYealinkID(tileList)
                self.strings = self.yealink(tileList)



    def astra(self, tileList):
        buttonStrings = []

        for tile in tileList:
            button = (str(tile.id) + "." + "type = " + str(tile.type) + "\n" +  
                      str(tile.id) + "." + "label = " + str(tile.label) + "\n" +
                      str(tile.id) + "." + "value = " + str(tile.value) + "\n")
            buttonStrings.append(button) 
        return buttonStrings



    def yealink(self, tileList):
        buttonStrings = []

        for tile in tileList:
            button = (str(tile.id) + "." + "type = " + str(tile.type) + "\n" + 
                      str(tile.id) + "." + "line = " + str(tile.line) + "\n" +  
                      str(tile.id) + "." + "value = " + str(tile.value) + "\n" + 
                      str(tile.id) + "." + "label = " + str(tile.label) + "\n")

            buttonStrings.append(button)
        return buttonStrings



    def setAastraID(self, tileList):
        for i, tile in enumerate(tileList):
            key = i + 1
            tile.id = "softkey" + str(key)



    def setYealinkID(self, tileList):
        for i, tile in enumerate(tileList):
            key = i+1
            tile.id = "linekey." + str(key)



    def setEXP40ID(self, tiles):
        for i, tile in enumerate(tiles):
            key = i+1
            tile.id = "expansion_module.1.key." + str(key)



    def makeReturnString(self, buttons):
        result = ""
        for button in buttons:
            result.append(button)

        return result



    def getStrings(self):
        print("getStrings")
        return self.strings
