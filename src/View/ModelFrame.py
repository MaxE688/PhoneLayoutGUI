"""


"""
import tkinter as tk
from tkinter import ttk
from Controller.MouseManager import MouseManager
from Controller.EditTileManager import EditTileManager
from Controller.PageLayout import PageLayout
from Model.constants import phoneModels
from Model.Tile import Tile

class ModelFrame(ttk.Frame):

    def __init__(self, tfManager, tiles):
        super().__init__(tfManager.pageContainer)
        self.tiles = tiles
        self.frameManager = tfManager
        self.model = tfManager.model
        self.mouseManager = MouseManager(self, self.frameManager)


        for t in tiles:
            t.setParent(self)
        self.layoutManager = PageLayout(self, tfManager.model, tiles)


    def makeDragable(self):
        for tile in self.tiles:
            self.mouseManager.addDraggable(tile)

    def makeEditable(self):
        for tile in self.tiles:
            self.mouseManager.addEditable(tile)


    def create(self):
        self.pack()

        print("Fetching Model Layout...")

    def redraw(self):
        self.layoutManager.redraw(self)

    def editTile(self, tile):
        EditTileManager(self, tile)


    def drag(self, widget, x, y):
        widget.place(x = x, y = y)

    def drop(self, dropped, x, y, col, row):
        dropped.place_forget()
        crushed = self.winfo_containing(x, y)

        if isinstance(crushed, Tile) and crushed != dropped:
            print("ModelFrame (drop): yes sir")
            self.layoutManager.shiftTiles(self.tiles, dropped, crushed)

        else:
            match(crushed):
                case self.layoutManager.nextPageTile:
                    shiftedTile = self.frameManager.toNextPage(self, dropped)
                    newTile = self.layoutManager.copyTile(self, shiftedTile)
                    self.tiles.remove(dropped)
                    self.tiles.append(newTile)
                case self.layoutManager.prevPageTile:
                    shiftedTile = self.frameManager.toPrevPage(self, dropped)

                    if shiftedTile != None:
                        newTile = self.layoutManager.copyTile(self, shiftedTile)

                        self.tiles.remove(dropped)
                        self.tiles.insert(0, newTile)
                    else:
                        self.frameManager.deletePage(self)


                case self.layoutManager.deleteTile:
                    self.tiles.remove(dropped)
                    dropped.destroy()

                    if len(self.tiles) == 0:
                        self.frameManager.deletePage(self)

                    elif self.frameManager.pageCount > 1:
                        # subList = self.frameManager.tilePageFrames
                        # shiftPageCount = len(self.frameManager.tilePageFrames[index:])
                        self.frameManager.deleteTileShift(self)




        self.redraw()
        self.frameManager.setID()

    def swapTilesNext(self, tile):
        return self.layoutManager.swapTilesNext(self, tile)

    def swapTilesPrev(self, tile):
        return self.layoutManager.swapTilesPrev(self, tile)

    def addTile(self):


        tile = Tile(
                        "",
                        "16",
                        "1",
                        "",
                        ""
                   )
        tile.setParent(self)
        self.mouseManager.addDraggable(tile)
        self.mouseManager.addEditable(tile)
        self.editTile(tile)

        if self.frameManager.pageCount > 1:
            tilesPerPage = phoneModels[self.model]['tilesPerPage'] - 1
        else:
            tilesPerPage = phoneModels[self.model]['tilesPerPage']


        if len(self.tiles) >= tilesPerPage:

            print()
            print("Current Page: " + str(self.frameManager.currentPage))
            print()

            index = 0
            if self.model == "Astra 6737i":
                index = 3

            self.tiles.insert(index, tile)
            lastTile = self.tiles.pop()
            self.frameManager.addTileShift(self, lastTile, tilesPerPage)
            self.frameManager.currentPage = self.frameManager.tilePageFrames.index(self)

            print()
            print("Current Page: " + str(self.frameManager.currentPage))
            print()

        else:
            self.tiles.append(tile)
        self.redraw()

        self.frameManager.setID()




    def test(self):
        print("Tiles List: ")
        for tile in self.tiles:
            print(str(self.tiles.index(tile)) + ": <" + tile.id + "> " + tile.label)

        for c in self.winfo_children():
            if isinstance(c, tk.Label) == False or isinstance(c, Tile):
                print(str(type(c)) + ": " + str(c.label if isinstance(c, Tile) else ""))
                print("\t(col, row): (" + str(c.grid_info()['column']) + ", " + str(c.grid_info()['row']) + ")")
            else:
                print(c['text'])



        # self.frameManager.setID()
