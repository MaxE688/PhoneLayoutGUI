

class ResultsGenerator:
    def __init__(self, tileList, brand):
        self.strings = ""
        match(brand):
            case "Astra":
                self.strings = self.astra(tileList)
                pass
            case "Yealink":
                self.strings = self.yealink(tileList)
                pass


    def astra(self, tileList):
        pass

    def yealink(self, tileList):
        buttonStrings = []

        for tile in tileList:
            button = (str(tile.id) + "." + "type = " + str(tile.type) + "\n" + 
                      str(tile.id) + "." + "line = " + str(tile.line) + "\n" +  
                      str(tile.id) + "." + "value = " + str(tile.value) + "\n" + 
                      str(tile.id) + "." + "label = " + str(tile.label) + "\n")

            buttonStrings.append(button)
        # return self.makeReturnString(buttonStrings)
        return buttonStrings

    def makeReturnString(self, buttons):
        result = ""
        for button in buttons:
            result.append(button)

        return result

    def getStrings(self):
        print("getStrings")
        return self.strings
