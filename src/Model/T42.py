import tkinter as tk

class T42:
    """used to arrange tiles in the layout for the Yealink T42
    
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
        self.numOfRows = 3

        #TODO: Why does this frame exist?
        self.f = tk.Frame(parent, width = 100)
        self.f.grid(column = 2, row = 4)
        
    

    def draw(self, tiles, pageCount):
        """draws all of thes page element
        
        Parameters
        ----------
        tiles : PageTile[]
        pageCount : int
        """

        for i, tile in enumerate(tiles):
            row = i % self.numOfRows
            if i >= self.numOfRows:
                col = 4
            else:
                col = 0
            tile.grid(column = col, row = row, sticky = 'nesw')

        if(pageCount > 1):
            self.layoutManager.reservedLabel.grid(column = 4, row = 2, sticky = 'nesw')
            self.layoutManager.nextPageTile.grid(column = 3, row = 1, rowspan = 2, sticky = 'w')
            self.layoutManager.prevPageTile.grid(column = 2, row = 1, rowspan = 2, sticky = 'e')
        self.layoutManager.deleteTile.grid(column = 2, row = 3, columnspan = 2)
        self.layoutManager.addTile.grid(column = 2, row = 0, columnspan = 2)
        self.layoutManager.printBtn.grid(column = 2, row = 5, columnspan = 2)
        self.f.grid(column = 2, row = 4, sticky = 'nesw')



