
import tkinter as tk
import re
from Model.constants import Brand, phoneModels
from View.EditTileFrame import EditTileFrame

class EditTileManager:
    """
    Controller for managing edits made to tiles

    Attributes
    ----------
    layoutManager : PageLayout
        instance of PageLayout used to submit edits to tile
    pageTile : PageTile
        instance of PageTile represents the tile being edited
    tile : Tile
        instance of Tile stored within pageTile
    brand : str
        the brand of the phone model selected
    typeOptions : dict(int, str)
        contains options available for the type of Tile used in dropdown menu
    editFrame : EditTileFrame
        instance of the frame that displays the edit form


    Methods
    -------
    getTypeOpts()
        returns the tile type options based on the brand of the phone model being edited
    astraTypeOptions()
        returns tile type options for Aastra phones
    yealinkTypeOptions()
        returns tile type options for Yealink phones
    getCurrOpt()
        returns the current type of the tile being edited
    updateTile(type : str, line : str, value : str, label : str)
        updates the values of the tile after an edit is complete
    submit()
        finalizes edits made to tile destroys instance of editFrame
    cancel()
        cancels edits made to tile destroys instance of editFrame

    """

    def __init__(self, layoutManager, model, tile):
        """
        Parameters
        ----------
        layoutManager : PageLayout
            Controller constructer was called from
        model : str
            model of the phone being edited
        tile : PageTile
            PageTile being edited 
        """
        
        self.layoutManager = layoutManager
        self.pageTile = tile
        self.tile = tile.tile
        self.brand = phoneModels[model]["brand"]
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
        
        options = self.getTypeOpts()
        currentOption = self.getCurrOpt()

        self.editFrame = EditTileFrame(tile, options, currentOption)
        self.editFrame.center()

        submitBtn = tk.Button(self.editFrame, text = "Submit")
        submitBtn['command'] = self.submit

        cancelBtn = tk.Button(self.editFrame, text = "Cancel")
        cancelBtn['command'] = self.cancel

        self.editFrame.setButtons( submitBtn, cancelBtn )
        self.editFrame.draw()



    def getTypeOpts(self):
        """returns the available options for the tile's type based on the brand of phone"""
        if self.brand == Brand.AASTRA.value:
            return self.astraTypeOptions()
        elif self.brand == Brand.YEALINK.value:
            return self.yealinkTypeOptions()



    def astraTypeOptions(self):
        """returns the available options for Aastra's tile's type"""
        return self.typeOptions.values()



    def yealinkTypeOptions(self):
        """returns the available options for Yealink's tile's type"""
        options = []
        for key in self.typeOptions.keys():
            options.append(str(key) + ": " + self.typeOptions[key])

        return options



    def getCurrOpt(self):
        """returns the current type of the tile being edited"""
        # print(self.tile.type)
        # print(type(self.tile.type))
        if self.brand == Brand.AASTRA.value:
            return str(self.tile.type)
        elif self.brand == Brand.YEALINK.value:
            option = str(self.tile.type) + ": "
            if type(self.tile.type) != "int":
                option += str(self.typeOptions[int(self.tile.type)])
            else:
                option += str(self.typeOptions[self.tile.type])
            # print()
            # print(option)
            # print()
            return option



    def updateTile(self, type, line, value, label):
        """updated the values of the tile being edited to the new values"""
        if self.brand == Brand.AASTRA.value:
            self.tile.type = type
        elif self.brand == Brand.YEALINK.value:
            self.tile.type = re.match("\d+", type)[0]
        self.tile.line = line
        self.tile.value = value
        self.tile.label = label
        #self.tile.setLabel(label)



    def submit(self):
        """submits edits made to the tile being edited"""
        self.updateTile(
            self.editFrame.getClicked(),
            self.editFrame.getLineBox(),
            self.editFrame.getValueEntry(),
            self.editFrame.getLabelEntry()
        )
        
        self.editFrame.destroy()
        self.layoutManager.submitEdit(self.pageTile.index)



    def cancel(self):
        """cancels the edit"""
        self.editFrame.destroy()

    
