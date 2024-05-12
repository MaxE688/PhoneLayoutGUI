import tkinter as tk
from tkinter import ttk
from Model.Tile import Tile


class EXP40:
    def __init__(self, layoutManager, parent):

        self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 10


    def draw(self, tiles):

        for i, tile in enumerate(tiles):
            row = i % self.numOfRows
            if i >= self.numOfRows:
                col = 4
            else:
                col = 0
            tile.grid(column = col, row = row)
        #Put tiles in right spot

        if(self.parent.frameManager.pageCount > 1):
            self.layoutManager.reservedLabel.grid(column = 4, row = 9)
            self.layoutManager.nextPageTile.grid(column = 3, row = 1, rowspan = 2)
            self.layoutManager.prevPageTile.grid(column = 2, row = 1, rowspan = 2)
        self.layoutManager.deleteTile.grid(column = 2, row = 3, columnspan = 2)
        self.layoutManager.addTile.grid(column = 2, row = 0, columnspan = 2)
