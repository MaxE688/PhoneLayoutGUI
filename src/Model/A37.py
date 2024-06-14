import tkinter as tk

class A37:

    def __init__(self, layoutManager, parent, topTiles):
        self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 6
        self.topTiles = topTiles
       
        self.f1 = tk.Frame(parent, width = 100)
        self.f1.grid(column = 2, row = 3)

        self.f2 = tk.Frame(parent, width = 100)
        self.f2.grid(column = 2, row = 4)


  
    def getTopKeyFrame(self):
        return self.f1



    def getSoftKeys(self, pageTiles):
        keys = []
        for page in pageTiles:
            if page.tile.id[0:4] == "soft":
                keys.append(page)
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



    def draw(self, tiles, pageCount, topKeys = None):
        softkeys = self.getSoftKeys(tiles)
        self.drawTopKeys(topKeys)
        self.drawKeys(softkeys)

        if pageCount > 1:
            self.layoutManager.reservedLabel.grid(column = 4, row = 5)
            self.layoutManager.nextPageTile.grid(column = 3, row = 1, rowspan = 2)
            self.layoutManager.prevPageTile.grid(column = 2, row = 1, rowspan = 2)
        self.layoutManager.deleteTile.grid(column = 2, row = 3, columnspan = 2)
        self.layoutManager.addTile.grid(column = 2, row = 1, columnspan = 2)
        self.layoutManager.printBtn.grid(column = 2, row = 6, columnspan = 2)
        self.f1.grid(column = 2, row = 0, sticky = "nesw")
        self.f2.grid(column = 2, row = 4, sticky = "nesw")

    
