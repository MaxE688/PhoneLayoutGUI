
from tkinter import ttk
from Model.PageTile import PageTile

class PageFrame(ttk.Frame):

    def __init__(self, parent, pageLayout, pageTiles):

        super().__init__(parent)

        self.tiles = pageTiles
        self.activeTiles = pageTiles
        self.pageLayout = pageLayout



    def setTiles(self, pageTiles):
        self.tiles = pageTiles



    def getTiles(self):
        return self.tiles



    def create(self):
        self.pack()
        print("Fetching Model Layout...")



    # def redraw(self):
    #     # self.layout.redraw(self)
    #     pass



    def updateLabels(self, firstIndex, tiles):
        self.activeTiles = []

        for i, tile in enumerate(tiles):
            if i > 26:
                pass
            if i >= len(self.tiles): 
                updatedTile = PageTile(firstIndex + i, tile)
                updatedTile.setParent(self.pageLayout.pageFrame)
                self.pageLayout.setMouseManager(updatedTile)
            else:
                self.tiles[i].updateValues( firstIndex + i, tile, tile.label)
                updatedTile = self.tiles[i]
            self.activeTiles.append(updatedTile)

        return self.activeTiles



    def test(self):
        print("Tiles List: ")
        for tile in self.activeTiles:
            print(str(self.tiles.index(tile)) + ": <" + tile.tile.id + "> " + tile.tile.label)


