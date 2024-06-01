import tkinter as tk
from tkinter import ttk
from Model.Tile import Tile


class T48:
    def __init__(self, layoutManager, parent):

        self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 6
        #Columns -> [0-4]

        self.f = tk.Frame(parent, width=100)
        self.f.grid(column = 2, row = 4)

    def draw(self, tiles, pageCount):
        col = 0
        nextCol = 4
        for i, tile in enumerate(tiles):
            row = i % self.numOfRows
            if i >= self.numOfRows and i < self.numOfRows * 2:
                tile.grid(column = 4, row = row)
                # col = 0
                nextCol = 1
            else:
                tile.grid(column = col, row = row)

            if row == self.numOfRows - 1:
                col = nextCol
                nextCol += 1
        #Put tiles in right spot

        if(pageCount > 1):
            self.layoutManager.reservedLabel.grid(column = 4, row = 5)

            # if

            self.layoutManager.nextPageTile.grid(column = 3, row = 7, rowspan = 2)
            self.layoutManager.prevPageTile.grid(column = 1, row = 7, rowspan = 2)
        self.layoutManager.deleteTile.grid(column = 2, row = 7)
        self.layoutManager.addTile.grid(column = 2, row = 6)
        self.f.grid(column = 2, row = 4, sticky = 'nesw')
