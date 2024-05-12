import tkinter as tk
from Model.Tile import Tile
from Model.A37 import A37
from Model.A39 import A39
from Model.T42 import T42
from Model.T46 import T46
from Model.T48 import T48
from Model.EXP40 import EXP40

class PageLayout:
    def __init__(self, parent, model, tiles):
        self.parent = parent
        self.model = model
        self.tiles = tiles

        self.tilePage = self.getTilePageFrame(model, parent)
        # if isinstance(self.tilePage, A37):
        #     self.parent.

        self.nextPageTile = tk.Label(parent, relief = tk.RAISED, text = 'Move to\nnext page', height = 4, width = 10)
        self.prevPageTile = tk.Label(parent, relief = tk.RAISED, text = 'Move to\nprev page', height = 4, width = 10)
        self.reservedLabel = tk.Label(parent, relief = tk.RAISED, text = 'Reserved', height = 4, width = 10)
        self.deleteTile = tk.Label(parent, relief = tk.RAISED, text = 'Delete Button', height  = 4, width = 10)
        self.addTile = tk.Button(parent, text = 'Add Button', command = self.parent.addTile)
        self.printBtn = tk.Button(parent, text = "Print Children", command = self.parent.test)


        if self.tilePage.__class__.__name__ == "A37":
            self.tilePage.topkeys = self.tilePage.getTopKeys(self)

        self.tilePage.draw(self.tiles)


    def getTilePageFrame(self, model, parent):
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


    def swapTilesNext(self, frame, tile):
        incomingTile = self.copyTile(frame, tile)
        firstTile = self.tiles.pop(0)
        self.tiles.insert(0, incomingTile)
        self.redraw(frame)

        return firstTile

    def swapTilesPrev(self, frame, tile):
        incomingTile = self.copyTile(frame, tile)
        lastTile = self.tiles.pop()
        self.tiles.append(incomingTile)
        self.redraw(frame)

        return lastTile

    def shiftTiles(self, tiles, dropped, crushed):
        # self.tilePage.shiftTiles(tiles, dropped, crushed)
        index = tiles.index(crushed)

        if index >= len(tiles):
            tiles.append(dropped)
        else:
            tiles.insert(index, tiles.pop(tiles.index(dropped)))

        if isinstance(self.tilePage, A37):
            self.tiles = tiles
            self.tilePage.topkeys = self.tilePage.getKeys('top')
            self.tilePage.softkeys = self.tilePage.getKeys('soft')

    def forget(self, page):
        for child in page.winfo_children():
            child.grid_forget()

    def redraw(self, page):
        # self.tilePage.forget(page)
        self.forget(page)

        if self.__class__.__name__ == 'A37':
            self.tilePage.topkeys = self.tilePage.getTopKeys(self)
            
        self.tilePage.draw(page.tiles)

    def copyTile(self, parent, widget):
        tile = Tile(
                    widget.id,
                    widget.type,
                    widget.line,
                    widget.value,
                    widget.label,
                   )
        tile.setParent(parent)
        parent.mouseManager.addDraggable(tile)
        parent.mouseManager.addEditable(tile)
        widget.destroy()


        return tile
