"""


"""
import tkinter as tk
from tkinter import ttk
from Controller.MouseManager import MouseManager
# from Controller.EditTileManager import EditTileManager
# from Controller.PageLayout import PageLayout
from Model.constants import phoneModels
from Model.Tile import Tile

class PageFrame(ttk.Frame):

    def __init__(self, parent, pageLayout, mouseManager, pageTiles):
        super().__init__(parent)

        # self.tiles is list[PageTile] (tileLabels)
        self.tiles = pageTiles



        # self.layout = pageLayout
        # self.model = parent
        # self.mouseManager = MouseManager(self, self.frameManager)


        for t in pageTiles:
            t.setParent(self)
            mouseManager.addDraggable(t)
            mouseManager.addEditable(t)

        # self.layoutManager = PageLayout(self, parent, tiles)
        # pageLayout.draw(self.tiles)

    def setTiles(self, pageTiles):
        self.tiles = pageTiles

    def getTiles(self):
        return self.tiles

    def create(self):
        self.pack()
        print("Fetching Model Layout...")

    def redraw(self):
        # self.layout.redraw(self)
        pass


    # update: index, tile, label
    def updateLabels(self, firstIndex, tiles):
        self.activeTiles = []
        for i, tile in enumerate(tiles):
            self.tiles[i].updateValues( firstIndex + i, tile, tile.label)
            self.activeTiles.append(self.tiles[i])
            # print(i)
            # tile.updateValues(firstIndex + i, tile, tile.label)
        return self.activeTiles



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








    # def editTile(self, tile):
    #     etm = EditTileManager(self, tile)
    #     # etm.editFrame.center()


    # def makeDragable(self):
    #     for tile in self.tiles:
    #         self.mouseManager.addDraggable(tile)

    # def makeEditable(self):
    #     for tile in self.tiles:
    #         self.mouseManager.addEditable(tile)

    # def drag(self, widget, x, y):
    #     widget.place(x = x, y = y)

    # def drop(self, dropped, x, y, col, row):
    #     dropped.place_forget()
    #     crushed = self.winfo_containing(x, y)

    #     if isinstance(crushed, Tile) and crushed != dropped:
    #         print("ModelFrame (drop): yes sir")
    #         self.layoutManager.shiftTiles(self.tiles, dropped, crushed)

    #     else:
    #         match(crushed):
    #             case self.layoutManager.nextPageTile:
    #                 shiftedTile = self.frameManager.toNextPage(self, dropped)
    #                 newTile = self.layoutManager.copyTile(self, shiftedTile)
    #                 self.tiles.remove(dropped)
    #                 self.tiles.append(newTile)
    #             case self.layoutManager.prevPageTile:
    #                 shiftedTile = self.frameManager.toPrevPage(self, dropped)

    #                 if shiftedTile != None:
    #                     newTile = self.layoutManager.copyTile(self, shiftedTile)

    #                     self.tiles.remove(dropped)
    #                     self.tiles.insert(0, newTile)
    #                 else:
    #                     self.frameManager.deletePage(self)


    #             case self.layoutManager.deleteTile:
    #                 self.tiles.remove(dropped)
    #                 dropped.destroy()

    #                 if len(self.tiles) == 0:
    #                     self.frameManager.deletePage(self)
    #                 elif self.frameManager.pageCount == 2 & len(self.tiles) == 1:
    #                     pass

    #                 elif self.frameManager.pageCount > 1:
    #                     # subList = self.frameManager.tilePageFrames
    #                     # shiftPageCount = len(self.frameManager.tilePageFrames[index:])
    #                     self.frameManager.deleteTileShift(self)




    #     self.redraw()
    #     self.frameManager.setID()

    # def swapTilesNext(self, tile):
    #     return self.layoutManager.swapTilesNext(self, tile)

    # def swapTilesPrev(self, tile):
    #     return self.layoutManager.swapTilesPrev(self, tile)

    # def addTile(self):


    #     tile = Tile(
    #                     "",
    #                     "16",
    #                     "1",
    #                     "",
    #                     ""
    #                )
    #     tile.setParent(self)
    #     self.mouseManager.addDraggable(tile)
    #     self.mouseManager.addEditable(tile)
    #     self.editTile(tile)

    #     if self.frameManager.pageCount > 1:
    #         tilesPerPage = phoneModels[self.model]['tilesPerPage'] - 1
    #     else:
    #         tilesPerPage = phoneModels[self.model]['tilesPerPage']


    #     if len(self.tiles) >= tilesPerPage:

    #         print()
    #         print("Current Page: " + str(self.frameManager.currentPage))
    #         print()

    #         index = 0
    #         if self.model == "Astra 6737i":
    #             index = 3

    #         self.tiles.insert(index, tile)
    #         lastTile = self.tiles.pop()
    #         self.frameManager.addTileShift(self, lastTile, tilesPerPage)
    #         self.frameManager.currentPage = self.frameManager.tilePageFrames.index(self)

    #         print()
    #         print("Current Page: " + str(self.frameManager.currentPage))
    #         print()

    #     else:
    #         self.tiles.append(tile)
    #     self.redraw()

    #     self.frameManager.setID()




