import tkinter as tk

class T48:
    """used to arrange tiles in the layout for the Yealink T48
    
    Attribute
    ---------
    layoutManager : PageLayout
        instance of controller that creates model layout class
    numOfRows : int
        the number of rows this model has

    Methods
    -------
    draw(tiles : PageTile, PageCount : int)
        draws all of the page elements
    """

    def __init__(self, layoutManager, parent):
        """
        Parameters
        ----------
        layoutManager : PageLayout
        """

        # self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 6

        # TODO: why does this exist?
        self.f = tk.Frame(parent, width=100)
        #self.f.grid(column = 2, row = 4)



    def draw(self, tiles, pageCount):
        """draws all of thes page element
        
        Parameters
        ----------
        tiles : PageTile[]
        pageCount : int
        """

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
            self.layoutManager.nextPageTile.grid(column = 3, row = 7, rowspan = 2)
            self.layoutManager.prevPageTile.grid(column = 1, row = 7, rowspan = 2)
        self.layoutManager.deleteTile.grid(column = 2, row = 7)
        self.layoutManager.addTile.grid(column = 2, row = 6)
       # self.f.grid(column = 2, row = 4, sticky = 'nesw')
