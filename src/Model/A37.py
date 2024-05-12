import tkinter as tk
from tkinter import ttk
from Model.Tile import Tile

class A37:
    def __init__(self, layoutManager, parent):
        self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 6
        # self.topkeys = self.getTopKeys(layoutManager.parent.frameManager.tilePageFrames[0], 'top')
        self.topkeys = self.getKeys( 'top')

    def getTopKeys(self, page):
        keys = []
        for tile in page.tiles:
            if tile.id[0:3] == 'top':
                keys.append(tile)
        return keys

    def getKeys(self, key):
        keys = []
        match(key):
            case 'top':
                for tile in self.layoutManager.tiles:
                    if tile.id[0:3] == key:
                        keys.append(tile)
            case 'soft':
                for tile in self.layoutManager.tiles:
                    if tile.id[0:4] == key:
                        keys.append(tile)
        return keys

    def drawTopKeys(self, tiles):
        for i, tile in enumerate(tiles):
            row = i % 3
            if i >= 3:
                col = 4
            else:
                col = 0
            tile.grid(column = col, row = row)

    def drawKeys(self, tiles):
        for i, tile in enumerate(tiles):
            row = (i % 3) + 3
            if i >= 3:
                col = 4
            else:
                col = 0
            tile.grid(column = col, row = row)


    def draw(self, tiles):
        self.drawTopKeys(self.topkeys)
        softkeys = self.getKeys('soft')
        self.drawKeys(softkeys)

        if self.parent.frameManager.pageCount > 1:
            self.layoutManager.reservedLabel.grid(column = 4, row = 5)
            self.layoutManager.nextPageTile.grid(column = 3, row = 1, rowspan = 2)
            self.layoutManager.prevPageTile.grid(column = 2, row = 1, rowspan = 2)
        self.layoutManager.deleteTile.grid(column = 2, row = 3, columnspan = 2)
        self.layoutManager.addTile.grid(column = 2, row = 0, columnspan = 2)
        self.layoutManager.printBtn.grid(column = 2, row = 6, columnspan = 2)
