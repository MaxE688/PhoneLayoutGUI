import tkinter as tk
from Model.Tile import Tile
from Model.A37 import A37
from Model.A39 import A39
from Model.T42 import T42
from Model.T46 import T46
from Model.T48 import T48
from Model.EXP40 import EXP40
from Model.constants import phoneModels
from Controller.ListManager import ListManager
from Model.PageTile import PageTile
from View.PageFrame import PageFrame
from Controller.MouseManager import MouseManager

class PageLayout:
    def __init__(self, tilePageContainerFrame, model, listManager:ListManager):
        self.parent = tilePageContainerFrame
        self.model = model
        self.listManager = listManager
        tileLabels = listManager.createPageTiles(0, phoneModels[model]["tilesPerPage"])
        self.mouseManager = MouseManager(self)
        self.pageFrame = PageFrame(self.parent, self, self.mouseManager, tileLabels)
        
        # Draws widgets to PageFrame
        self.modelLayout = self.getModelLayout(model, self.pageFrame)


        self.nextPageTile = tk.Label(   self.pageFrame, relief = tk.RAISED, text = 'Move to\nnext page', height = 4, width = 10)
        self.prevPageTile = tk.Label(   self.pageFrame, relief = tk.RAISED, text = 'Move to\nprev page', height = 4, width = 10)
        self.reservedLabel = tk.Label(  self.pageFrame, relief = tk.RAISED, text = 'Reserved', height = 4, width = 10)
        self.deleteTile = tk.Label(     self.pageFrame, relief = tk.RAISED, text = 'Delete Button', height  = 4, width = 10)
        self.addTile = tk.Button(       self.pageFrame, text = 'Add Button', command = self.listManager.addTile)
        self.printBtn = tk.Button(      self.pageFrame, text = "Print Children", command = self.listManager.test)



        

        if self.modelLayout.__class__.__name__ == "A37":
            self.modelLayout.topkeys = self.modelLayout.getTopKeys(self)

        # self.modelLayout.draw(self.tiles)
        self.draw(self.pageFrame.getTiles())
        self.pageFrame.create()





    def getModelLayout(self, model, parent):
        match(model):
            case "Astra 6737i":
                return A37(self, parent)
            case "Astra 6739i":
                return A39(self, parent)
            case "Yealink T48":
                return T48(self, parent)
            case "Yealink T46":
                return T46(self, parent)
            case "Yealink T42":
                return T42(self, parent)
            case "Yealink T41":
                return T42(self, parent)
            case "Yealink EXP40":
                return EXP40(self, parent)


    def draw(self, tiles):
        self.modelLayout.draw(tiles, self.listManager.getPageCount())

    def forget(self, page):
        for child in page.winfo_children():
            child.grid_forget()

    def redraw(self, page: PageFrame, pageFirstIndex):
        # self.tilePage.forget(page)
        # self.forget(page)

        # pageSize = self.listManager.getPageSize()
        # pageTiles = self.listManager.getPageTiles(pageFirstIndex, pageSize)
        
        # for tile in pageTiles:
        #     tile.setParent(page)

        tiles = self.listManager.getPageTiles(pageFirstIndex)
        page.updateLabels(pageFirstIndex, tiles)
        # page.setTiles(pageTiles) #NEED: startIndex, pageSize

        if self.__class__.__name__ == 'A37':
            self.modelLayout.topkeys = self.modelLayout.getTopKeys(self)
            
        self.modelLayout.draw(page.tiles, self.listManager.getPageCount())



        














    # def editTile(self, tile):
    #     etm = EditTileManager(self, tile)
    #     # etm.editFrame.center()


    def drag(self, widget, x, y):
        widget.place(x = x, y = y)

    def drop(self, dropped, x, y, col, row):
        dropped.place_forget()
        crushed = self.pageFrame.winfo_containing(x, y)
        # crushed = dropped.parent.winfo_containing(x, y)
        # crushed = self.winfo_containing(x, y)

        if isinstance(crushed, PageTile) and crushed != dropped:
            print("ModelFrame (drop): yes sir")
            # self.layoutManager.shiftTiles(self.listManager, dropped, crushed)
            
            # Removes dropped tile from list, inserts dropped tile into crushed tile's position
            self.listManager.shiftTile(dropped.index, crushed.index)
            self.redraw(self.pageFrame, self.listManager.getPageFirstTile(crushed.index))
            

        # else:
        #     match(crushed):
        #         case self.layoutManager.nextPageTile:
        #             shiftedTile = self.frameManager.toNextPage(self, dropped)
        #             newTile = self.layoutManager.copyTile(self, shiftedTile)
        #             self.listManager.remove(dropped)
        #             self.listManager.append(newTile)
        #         case self.layoutManager.prevPageTile:
        #             shiftedTile = self.frameManager.toPrevPage(self, dropped)

        #             if shiftedTile != None:
        #                 newTile = self.layoutManager.copyTile(self, shiftedTile)

        #                 self.listManager.remove(dropped)
        #                 self.listManager.insert(0, newTile)
        #             else:
        #                 self.frameManager.deletePage(self)
                
        #         case self.layoutManager.deleteTile:
        #             self.listManager.remove(dropped)
        #             dropped.destroy()

        #             if len(self.listManager) == 0:
        #                 self.frameManager.deletePage(self)
        #             elif self.frameManager.pageCount == 2 & len(self.listManager) == 1:
        #                 pass

        #             elif self.frameManager.pageCount > 1:
        #                 # subList = self.frameManager.tilePageFrames
        #                 # shiftPageCount = len(self.frameManager.tilePageFrames[index:])
        #                 self.frameManager.deleteTileShift(self)




























        
    # def swapTilesNext(self, frame, tile):
    #     incomingTile = self.copyTile(frame, tile)
    #     firstTile = self.tiles.pop(0)
    #     self.tiles.insert(0, incomingTile)
    #     self.redraw(frame)

    #     return firstTile

    # def swapTilesPrev(self, frame, tile):
    #     incomingTile = self.copyTile(frame, tile)
    #     lastTile = self.tiles.pop()
    #     self.tiles.append(incomingTile)
    #     self.redraw(frame)

    #     return lastTile

    # def shiftTiles(self, tiles, dropped, crushed):
    #     # self.tilePage.shiftTiles(tiles, dropped, crushed)
    #     index = tiles.index(crushed)

    #     if index >= len(tiles):
    #         tiles.append(dropped)
    #     else:
    #         tiles.insert(index, tiles.pop(tiles.index(dropped)))

    #     if isinstance(self.pageLayout, A37):
    #         self.tiles = tiles
    #         self.pageLayout.topkeys = self.pageLayout.getKeys('top')
    #         self.pageLayout.softkeys = self.pageLayout.getKeys('soft')


    # def copyTile(self, parent, widget):
    #     tile = Tile(
    #                 widget.id,
    #                 widget.type,
    #                 widget.line,
    #                 widget.value,
    #                 widget.label,
    #                )
    #     tile.setParent(parent)
    #     parent.mouseManager.addDraggable(tile)
    #     parent.mouseManager.addEditable(tile)
    #     widget.destroy()


    #     return tile
