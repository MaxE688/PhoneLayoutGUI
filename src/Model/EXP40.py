import tkinter as tk

class EXP40:
    """
    used to arrange tiles in the layout for the Yealink EXP40 sidecar 

    Attributes
    ----------
    parent : PageFrame
        parent frame for f Frame
    layoutManager : PageLayout
        instance of controller that creates model layout class
    numOfRows : int
        the number of rows supported by exp40 model
    f : tk.Frame
        a frame being drawn for some reason

    Methods
    -------
    draw(tiles : PageTile[], pageCount : int)
        draws all of the pages elements to window

    """

    def __init__(self, layoutManager, parent):
        """
        Parameters
        ----------
        layoutManager : PageLayout
        parent : PageFrame
        """
        self.parent = parent
        self.layoutManager = layoutManager
        self.numOfRows = 10

        #TODO: why does this frame exist???
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
            tile.grid(column = col, row = row)
        #Put tiles in right spot

        if(pageCount > 1):
            self.layoutManager.reservedLabel.grid(column = 4, row = 9)
            self.layoutManager.nextPageTile.grid(column = 3, row = 1, rowspan = 2)
            self.layoutManager.prevPageTile.grid(column = 2, row = 1, rowspan = 2)
        self.layoutManager.deleteTile.grid(column = 2, row = 3, columnspan = 2)
        self.layoutManager.addTile.grid(column = 2, row = 0, columnspan = 2)
