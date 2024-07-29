from Controller.ListManager import ListManager
from Model.Tile import Tile
from Model.constants import Brand, Model, phoneModels

class ResultsGenerator:
    """
    Controller responsible for converting tile objects into output config string

    Attributes
    ----------
    strings : str
        final config string to be output to user

    Methods
    -------
    astra(tileList : Tile[])
        returns list with each element being the configuration of a single button for Aastra phones
    yealink(tileList : Tile[])
        returns list with each element being the configuration of a single button for Yealink phones
    setAastraID(tileList : Tile[])
        gives each button config string the correct prefix for Aastra phones
    setYealinkID(tileList : Tile[])
        gives each button config string the correct prefix for Yealink phones
    setEXP40ID(tiles : Tile[])
        gives each button config string the correct prefix for the Yealink EXP40 model
    getStrings()
        returns the final output config string

    """
    def __init__(self, listManager: ListManager, model: str):
        """
        Parameters
        ----------
        listManager : ListManager
        model : str
        """
        
        brand = phoneModels[model]["brand"]
        self.strings = ""
        match(brand):
            case Brand.AASTRA.value:
                tiles = []
                if model == Model.AASTRA_6737.value:
                    for tile in listManager.topTiles:
                        tiles.append(tile.tile)
                tiles.extend(listManager.tiles)

                self.setAastraID(tiles)
                self.strings = self.astra(tiles)
            case Brand.YEALINK.value:
                if model == Model.YEALINK_EXP40.value:
                    self.setEXP40ID(listManager.tiles)
                else:
                    self.setYealinkID(listManager.tiles)
                self.strings = self.yealink(listManager.tiles)



    def astra(self, tileList):
        """Converts tiles to button config strings for Aastra phones
        
        Parameters
        ----------
        tileList : Tile[]
        """

        buttonStrings = []

        for tile in tileList:
            button = (str(tile.id) + " " + "type: " + str(tile.type) + "\n" +  
                      str(tile.id) + " " + "label: " + str(tile.label) + "\n" +
                      str(tile.id) + " " + "value: " + str(tile.value) + "\n")
            buttonStrings.append(button) 
        return buttonStrings



    def yealink(self, tileList):
        """Converts tiles to button config strings for Yealink phones
        
        Parameters
        ----------
        tileList : Tile[]
        """

        buttonStrings = []

        for tile in tileList:
            button = (str(tile.id) + "." + "type = " + str(tile.type) + "\n" + 
                      str(tile.id) + "." + "line = " + str(tile.line) + "\n" +  
                      str(tile.id) + "." + "value = " + str(tile.value) + "\n" + 
                      str(tile.id) + "." + "label = " + str(tile.label) + "\n")

            buttonStrings.append(button)
        return buttonStrings



    def setAastraID(self, tileList: list[Tile]):
        """Gives each tile the correct prefix for Aastra phones
        
        Parameters
        ----------
        tileList : Tile[]
        """

        topKey = 0
        softkey = 0
        for i, tile in enumerate(tileList):
            if tile.id[:3] == "top":
                keyType = "topsoftkey"
                topKey += 1
                key = topKey
            else:
                keyType = "softkey"
                softkey += 1
                key = softkey
            
            tile.id = keyType + str(key)



    def setYealinkID(self, tileList):
        """Gives each tile the correct prefix for Yealink phones
        
        Parameters
        ----------
        tileList : Tile[]
        """

        for i, tile in enumerate(tileList):
            key = i+1
            tile.id = "linekey." + str(key)



    def setEXP40ID(self, tiles):
        """Gives each tile the correct prefix for Yealink EXP40 side car
        
        Parameters
        ----------
        tiles : Tile[]
        """

        for i, tile in enumerate(tiles):
            key = i+1
            tile.id = "expansion_module.1.key." + str(key)



    # def makeReturnString(self, buttons):
    #     result = ""
    #     for button in buttons:
    #         result.append(button)

    #     return result



    def getStrings(self):
        """Returns final output config string"""
    
        return self.strings
