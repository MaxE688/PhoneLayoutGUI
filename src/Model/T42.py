import tkinter as tk
from tkinter import ttk
from Model.Tile import Tile

class T42:
    def __init__(self, layoutManager, parent):

        # self.tilesPerPage = phoneModels[parent.frameManager.model]['tilesPerPage']
        # self.tiles = tiles
        self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 3

        self.f = tk.Frame(parent, width = 100)
        self.f.grid(column = 2, row = 4)

    def draw(self, tiles):
        for i, tile in enumerate(tiles):
            row = i % self.numOfRows
            if i >= self.numOfRows:
                col = 4
            else:
                col = 0
            tile.grid(column = col, row = row, sticky = 'nesw')

        if(self.parent.frameManager.pageCount > 1):
            self.layoutManager.reservedLabel.grid(column = 4, row = 2, sticky = 'nesw')
            self.layoutManager.nextPageTile.grid(column = 3, row = 1, rowspan = 2, sticky = 'w')
            self.layoutManager.prevPageTile.grid(column = 2, row = 1, rowspan = 2, sticky = 'e')
        self.layoutManager.deleteTile.grid(column = 2, row = 3, columnspan = 2)
        self.layoutManager.addTile.grid(column = 2, row = 0, columnspan = 2)
        self.layoutManager.printBtn.grid(column = 2, row = 5, columnspan = 2)
        self.f.grid(column = 2, row = 4, sticky = 'nesw')
