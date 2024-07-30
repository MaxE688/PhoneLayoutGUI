import tkinter as tk

from Model.PageTile import PageTile

class A37:
    """used to arrange tiles in the layout for the Aastra 6737i
    
    Attributes
    ----------
    parent : PageFrame
        parent frame of f1, and f2 frames
    layoutManager : PageLayout
        instance of controller that creates model layout class
    numOfRows : int
        the number of rows 
    topTiles : PageTile[]
        list of top tiles used with Aastra 6737i 
    f1 : tk.Frame
        frame that contains toptiles
    f2 : tk.Frame
        frame that contains normal tiles
    
    Methods
    -------
    getTopKeyFrame()
        returns the frame that contains toptiles (topsoftkeys)
    getSoftKeys(pageTiles : PageTile[])
        seperates topsoftkeys from softkeys, and returns list of softkeys
    drawTopKeys(tiles : PageTile[])
        places topkeys in their correct position
    drawKeys(tiles : PageTile[])
        places keys in their correct position
    draw(tiles : PageTile[], pageCount : int, topKeys : None | PageTile[])
        draws all of the page elements 

    """

    def __init__(self, layoutManager, parent, topTiles):
        """
        Parameters
        ----------
        layoutManager : PageLayout
        parent : PageFrame
        topTiles : PageTile[]
        """

        self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 6
        self.topTiles = topTiles
       
        self.f1 = tk.Frame(parent, width = 100)
        self.f1.grid(column = 2, row = 3)

        self.f2 = tk.Frame(parent, width = 100)
        self.f2.grid(column = 2, row = 4)


  
    def getTopKeyFrame(self):
        """return frame that contains topkeys"""

        return self.f1



    def getSoftKeys(self, pageTiles):
        """returns list of all softkeys
        
        Parameters
        ----------
        pageTiles : PageTile[]
        """

        keys = []
        for page in pageTiles:
            if page.tile.id[0:3] != "top":
                keys.append(page)
        return keys
    


    def drawTopKeys(self, tiles: list[PageTile]):
        """draws topkeys to window
        
        Parameters
        ----------
        tiles : PageTile[]
        """

        for i, tile in enumerate(tiles):
            row = i % 3
            if i >= 3:
                col = 4
            else:
                col = 0
            #print(type(tile))
            tile.grid(column = col, row = row)



    def drawKeys(self, tiles: list[PageTile]):
        """draws keys to window
        
        Parameters
        ----------
        tiles : PageTile[]
        """

        for i, tile in enumerate(tiles):
            row = (i % 3) + 3
            if i >= 3:
                col = 4
            else:
                col = 0
            tile.grid(column = col, row = row)
            


    def draw(self, tiles, pageCount, topKeys = None):
        """draws all of the elements to window
        
        Parameters
        ----------
        tiles : PageTile[]
        pageCount : int
        topKeys : None | PageTile[]
            Optional parameter
        """

        softkeys = self.getSoftKeys(tiles)
        self.drawTopKeys(topKeys)
        self.drawKeys(softkeys)

        if pageCount > 1:
            self.layoutManager.reservedLabel.grid(column = 4, row = 5)
            self.layoutManager.nextPageTile.grid(column = 3, row = 2, rowspan = 2)
            self.layoutManager.prevPageTile.grid(column = 2, row = 2, rowspan = 2)
        self.layoutManager.deleteTile.grid(column = 2, row = 4, columnspan = 2)
        self.layoutManager.addTile.grid(column = 2, row = 1, columnspan = 2)
        self.layoutManager.printBtn.grid(column = 2, row = 6, columnspan = 2)
        self.f1.grid(column = 2, row = 0, sticky = "nesw")
        self.f2.grid(column = 2, row = 4, sticky = "nesw")

    
