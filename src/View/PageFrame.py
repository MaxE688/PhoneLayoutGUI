
from tkinter import ttk
from Model.PageTile import PageTile

class PageFrame(ttk.Frame):
    """
    frame for the current page being displayed

    Attribute
    ---------
    tiles : PageTile[]
        page tiles that belong to the page
    activeTiles : PageTile[]
        list of page tiles that need to have their values updated
    pageLayout : PageLayout[]
        controller that manages page frame
    Methods
    -------
    setTiles(pageTiles : PageTile[])
        set page tiles
    getTiles()
        returns list of tiles
    create()
        draws widgets
    updateLabels(firstIndex : int, tiles : PageTile)
        updates the values of the page tiles

    """

    def __init__(self, parent, pageLayout, pageTiles):
        """
        Parameters
        ----------
        parent : ttk.Frame
        pageLayout : PageLayout
        pageTiles : PageTile[]
        """

        super().__init__(parent)

        self.tiles = pageTiles
        self.activeTiles = pageTiles
        self.pageLayout = pageLayout



    def setTiles(self, pageTiles):
        """set tiles attribute
        
        Parameters
        ----------
        pageTiles : PageTile[]
        """

        self.tiles = pageTiles



    def getTiles(self):
        """returns list of page tiles"""

        return self.tiles



    def create(self):
        """create the frame"""

        self.pack()
        print("Fetching Model Layout...")



    # def redraw(self):
    #     # self.layout.redraw(self)
    #     pass



    def updateLabels(self, firstIndex, tiles):
        """update the values of the pagetiles that belong to this page
        
        Parameters
        ----------
        firstIndex : int
        tiles : PageTile[]
        """

        self.activeTiles = []

        for i, tile in enumerate(tiles):
            #TODO: why is this 26?
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


