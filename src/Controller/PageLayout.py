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
from Controller.EditTileManager import EditTileManager
from View.PageFrame import PageFrame
from Controller.MouseManager import MouseManager

class PageLayout:
    def __init__(self, pageFrameManager, tilePageContainerFrame, model, listManager:ListManager):
        self.pageFrameManager = pageFrameManager
        self.parent = tilePageContainerFrame
        self.model = model
        self.listManager = listManager
        self.currentPage = 0
        tileLabels = listManager.createPageTiles(0, phoneModels[model]["tilesPerPage"])
        self.mouseManager = MouseManager(self)


        self.pageFrame = PageFrame(self.parent, self, tileLabels)
        self.pageTileSetup(self.pageFrame, tileLabels)

        # Draws widgets to PageFrame
        self.modelLayout = self.getModelLayout(model, self.pageFrame)
        if self.modelLayout.topTiles:
            self.pageTileSetup(self.modelLayout.getTopKeyFrame(), self.listManager.topTiles)


        self.nextPageTile = tk.Label(   self.pageFrame, relief = tk.RAISED, text = 'Move to\nnext page', height = 4, width = 10)
        self.prevPageTile = tk.Label(   self.pageFrame, relief = tk.RAISED, text = 'Move to\nprev page', height = 4, width = 10)
        self.reservedLabel = tk.Label(  self.pageFrame, relief = tk.RAISED, text = 'Reserved', height = 4, width = 10)
        self.deleteTile = tk.Label(     self.pageFrame, relief = tk.RAISED, text = 'Delete Button', height  = 4, width = 10)
        self.addTile = tk.Button(       self.pageFrame, text = 'Add Button', command = self.addNewTile)
        # self.printBtn = tk.Button(      self.pageFrame, text = "Print Children", command = self.listManager.test)
        self.printBtn = tk.Button(      self.pageFrame, text = "Print Children", command = self.pageFrame.test)



        
        self.draw(self.pageFrame.getTiles())
        self.pageFrame.create()





    def getModelLayout(self, model, parent):
        match(model):
            case "Astra 6737i":
                return A37(self, parent, self.listManager.topTiles)
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
        if self.listManager.topTiles:
            self.modelLayout.draw(tiles, self.listManager.getPageCount(), self.listManager.topTiles )
        else:
            self.modelLayout.draw(tiles, self.listManager.getPageCount())

    # def forget(self, page):
    def forget(self):
        # for child in page.winfo_children():
        for child in self.pageFrame.winfo_children():
            child.grid_forget()

    def redraw(self, page: PageFrame, pageFirstIndex):
        self.forget()

        self.pageFrameManager.updatePageLabel(self.listManager.getPageOfIndex(pageFirstIndex), self.listManager.getPageCount())
        tiles = self.listManager.getPageTiles(pageFirstIndex)
        pageTiles = page.updateLabels(pageFirstIndex, tiles)

        self.draw(pageTiles)


    def nextPage(self):
        nextPageIndex = self.pageFrame.activeTiles[-1].index + 1
        if nextPageIndex < len(self.listManager.tiles):
            self.redraw(self.pageFrame, nextPageIndex)
        pass


    def prevPage(self):
        prevPageIndex = self.pageFrame.activeTiles[0].index - 1
        if prevPageIndex >= 0:
            prevPageIndex = self.listManager.getPageFirstTile(prevPageIndex)
            self.redraw(self.pageFrame, prevPageIndex)
        pass


    def addNewTile(self):
        endTile = self.listManager.tiles[-1]
    
        newTile = Tile(
            "",
            "16",
            "1",
            "",
            "New Tile"
        )
        # newPageTile = PageTile()
        # self.editTile(newTile)
        self.listManager.addTile(newTile)
        lastIndex = len(self.listManager.tiles) - 1
        pageFirstTile = self.listManager.getPageFirstTile(lastIndex) 
        self.redraw(self.pageFrame, pageFirstTile)

    def editTile(self, tile):
        EditTileManager(self, self.model, tile)


    def drag(self, widget, x, y):
        widget.place(x = x, y = y)

    def drop(self, dropped, x, y, col, row):
        droppedIndex = dropped.index
        dropped.place_forget()
        crushed = self.pageFrame.winfo_containing(x, y)

        if isinstance(crushed, PageTile) and crushed != dropped:
            print("ModelFrame (drop): yes sir")
            
            if dropped.tile.id[:3] == "top":
                self.listManager.shiftTopTile(dropped.index, crushed.index)
            else:
                # Removes dropped tile from list, inserts dropped tile into crushed tile's position
                self.listManager.shiftTile(dropped.index, crushed.index)
        else:
            match(crushed):
                case self.nextPageTile:
                    tiles = self.pageFrame.tiles
                    # lastIndex = self.pageFrame.tiles[-1]
                    lastIndex = self.pageFrame.activeTiles[-1]
                    self.listManager.toNextPage(dropped.index, lastIndex.index)
                    pass
                case self.prevPageTile:
                    firstIndex = self.pageFrame.tiles[0].index
                    self.listManager.toPrevPage(dropped.index, firstIndex)
                    pass
                case self.deleteTile:
                    # remove tile from list
                    self.listManager.deleteTile(dropped.tile)
                    pass
                case _:
                    # Reset dropped tile to original position
                    pass
        self.redraw(self.pageFrame, self.listManager.getPageFirstTile(droppedIndex))


    def cont(self):
        self.pageFrameManager.finish()



    def submitEdit(self, pageTile):
        self.redraw(self.pageFrame, self.listManager.getPageFirstTile(pageTile))


    def pageTileSetup(self, parent, tiles):
        for tile in tiles:
            tile.setParent(parent)
            self.mouseManager.addDraggable(tile)
            self.mouseManager.addEditable(tile)
    

    def setMouseManager(self, tile):
        self.mouseManager.addDraggable(tile)
        self.mouseManager.addEditable(tile)



