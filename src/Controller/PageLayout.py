import tkinter as tk
from Model.Tile import Tile
from Model.A37 import A37
from Model.A39 import A39
from Model.T42 import T42
from Model.T46 import T46
from Model.T48 import T48
from Model.EXP40 import EXP40
from Model.constants import Model, phoneModels
from Controller.ListManager import ListManager
from Model.PageTile import PageTile
from Controller.EditTileManager import EditTileManager
from View.PageFrame import PageFrame
from Controller.MouseManager import MouseManager

class PageLayout:
    """
    Controller for the layout of the current page's frame

    Attributes
    ----------
    pageFrameMangager : PageFrameManager
        instance of controller for this controller
    parent : ttk.Frame
        parent of page frame
    model : str
        model of the phone being edited 
    listManager : ListManager
        perform actions to list of tiles
    currentPage : int
        the page number of the current page being viewed
    mouseManager : MouseManager
        create mouse event listeners 
    pageFrame : PageFrame
        Frame used to display the current page
    modelLayout : A37 | A39 | EXP40 | T42 | T46 | T48
        layout of the pages to display, 
        each possible class represents the layout for the phone model being edited
    nextPageTile : tk.Label
        label for the drop area to send tile to next page
    prevPageTile : tk.Label
        label for the drop area to send tile to previous page
    deleteTile : tk.Label
        labe for the drop area to delete a tile
    addTile : tk.Button
        button used to add tiles to the list
    printBtn : tk.Button
        prints the frame's children to the console

    Methods
    -------
    getModelLayout(model : str, parent: ttk.Frame)
        creates instance of the appropriate phone model's layout
    draw(tiles : Tile[])
        draws tiles to the frame
    forget()
        forget self
    redraw(page: PageFrame, pageFirstIndex : int)
        update state before drawing again
    nextPage()
        displays the next page
    prevPage()
        displays the previous page
    addNewTile()
        creates a new Tile, and adds it to the list
    editTile(tile : PageTile)
        creates instance of EditTileManager
    drag(widget : ttk.Label | ttk.Button | tk.Frame, x : int, y : int)
        updates widget's location if widget is a Tile
    drop(dropped : ttk.Label | ttk.Button | tk.Frame, x : int, y : int)
        handles tile drop
    cont()
        called when self is no longer needed
    submitEdit(pageTileIndex : int)
        redraw tiles after an edit
    pageTileSetup(parent : PageFrame)
        gives parent to each tile, and binds functions to each tile 
    setMouseManager(tile : PageTIle)
        binds functions to the tile passed

    """

    def __init__(self, pageFrameManager, tilePageContainerFrame, model: str, listManager:ListManager):
        """
        Parameters
        ----------
        pageFrameManager : PageFrameManager
        tilePageContainerFrame : ttk.Frame
        model : str
        listManager : ListManager
        """

        self.pageFrameManager = pageFrameManager
        self.parent = tilePageContainerFrame
        self.model = model
        self.listManager = listManager
        self.currentPage = 0
        pageTiles = listManager.createPageTiles(0, phoneModels[model]["tilesPerPage"])
        self.mouseManager = MouseManager(self)

        self.pageFrame = PageFrame(self.parent, self, pageTiles)
        self.pageTileSetup(self.pageFrame, pageTiles)

        # Draws widgets to PageFrame
        self.modelLayout = self.getModelLayout(model, self.pageFrame)
        
        if model == Model.AASTRA_6737.value:
            self.pageTileSetup(self.modelLayout.getTopKeyFrame(), self.listManager.topTiles)

        self.nextPageTile = tk.Label(   self.pageFrame, relief = tk.RAISED, text = 'Move to\nnext page', height = 4, width = 10)
        self.prevPageTile = tk.Label(   self.pageFrame, relief = tk.RAISED, text = 'Move to\nprev page', height = 4, width = 10)
        self.reservedLabel = tk.Label(  self.pageFrame, relief = tk.RAISED, text = 'Reserved', height = 4, width = 10)
        self.deleteTile = tk.Label(     self.pageFrame, relief = tk.RAISED, text = 'Delete Button', height  = 4, width = 10)
        self.addTile = tk.Button(       self.pageFrame, text = 'Add Button', command = self.addNewTile)
        self.printBtn = tk.Button(      self.pageFrame, text = "Print Children", command = self.pageFrame.test)


        
        self.draw(self.pageFrame.getTiles())
        self.pageFrame.create()



    def getModelLayout(self, model, parent):
        """returns instance of correct phone model layout
        
        Parameters
        ----------
        model : str
        parent : PageFrame
        """
        match(model):
            case Model.AASTRA_6737.value:
                return A37(self, parent, self.listManager.topTiles)
            case Model.AASTRA_6739.value:
                return A39(self, parent)
            case Model.YEALINK_T48.value:
                return T48(self, parent)
            case Model.YEALINK_T46.value:
                return T46(self, parent)
            case Model.YEALINK_T42.value:
                return T42(self, parent)
            case Model.YEALINK_T41.value:
                return T42(self, parent)
            case Model.YEALINK_EXP40.value:
                return EXP40(self, parent)



    def draw(self, tiles):
        """draw widgets to display
        
        Parameters
        ----------
        tiles : Tile[]
        """

        if self.model == Model.AASTRA_6737.value:
            topTiles = self.listManager.getTopTiles()
            self.modelLayout.draw(tiles, self.listManager.getPageCount(), topTiles )
        else:
            self.modelLayout.draw(tiles, self.listManager.getPageCount())



    def forget(self):
        """forgets self"""
        for child in self.pageFrame.winfo_children():
            child.grid_forget()



    def redraw(self, page: PageFrame, pageFirstIndex):
        """updates state before drawing again
        
        Parameters
        ----------
        page : PageFrame
        pageFirstIndex : int
        """

        self.forget()

        self.pageFrameManager.updatePageLabel(self.listManager.getPageOfIndex(pageFirstIndex), self.listManager.getPageCount())
        tiles = self.listManager.getPageTiles(pageFirstIndex)
        pageTiles = page.updateLabels(pageFirstIndex, tiles)

        self.draw(pageTiles)



    def nextPage(self):
        """moves tile to next page"""
        if self.pageFrame.activeTiles:
            nextPageIndex = self.pageFrame.activeTiles[-1].index + 1
        else:
            nextPageIndex = phoneModels[self.model].tilesPerPage - 1
        if nextPageIndex < len(self.listManager.tiles):
            self.redraw(self.pageFrame, nextPageIndex)
        pass



    def prevPage(self):
        """moves tile to previous page"""
        prevPageIndex = self.pageFrame.activeTiles[0].index - 1
        if prevPageIndex >= 0:
            prevPageIndex = self.listManager.getPageFirstTile(prevPageIndex)
            self.redraw(self.pageFrame, prevPageIndex)
        pass



    def addNewTile(self):
        """adds a new tile to the list"""
        print("addNewTile called")
        endTile = self.listManager.tiles[-1]
    
        newTile = Tile(
            "",
            "16",
            "1",
            "",
            "New Tile"
        )

        self.listManager.addTile(newTile)
        lastIndex = len(self.listManager.tiles) - 1
        pageFirstTileIndex = self.listManager.getPageFirstTile(lastIndex) 
        self.redraw(self.pageFrame, pageFirstTileIndex)



    def editTile(self, tile):
        """opens EditTileManager to edit tile passed
        
        Parameters
        ----------
        tile : Tile
        """

        EditTileManager(self, self.model, tile)



    def drag(self, widget, x, y):
        """allows tile to be dragged
        
        Parameters
        ----------
        widget : ttk.Label | ttk.Button | tk.Frame 
        x : int 
        y : int
        """

        widget.place(x = x, y = y)



    def drop(self, dropped, x, y):
        """handles drop event
        
        Parameters
        ----------
        dropped : ttk.Label | ttk.Button | tk.Frame 
        x : int
        y : int
        """

        droppedIndex = dropped.index
        dropped.place_forget()
        crushed = self.pageFrame.winfo_containing(x, y)

        if isinstance(crushed, PageTile) and crushed != dropped:
            print("ModelFrame (drop)")
            
            if dropped.tile.id[:3] == "top":
                self.listManager.shiftTopTile(dropped.index, crushed.index)
            else:
                # Removes dropped tile from list, inserts dropped tile into crushed tile's position
                self.listManager.shiftTile(dropped.index, crushed.index)
        else:
            match(crushed):
                case self.nextPageTile:
                    tiles = self.pageFrame.tiles
                    # lastIndex = self.pageFrame.tiles[-1]
                    lastIndex = self.pageFrame.activeTiles[-1]
                    self.listManager.toNextPage(dropped.index, lastIndex.index)
                    pass
                case self.prevPageTile:
                    firstIndex = self.pageFrame.tiles[0].index
                    self.listManager.toPrevPage(dropped.index, firstIndex)
                    pass
                case self.deleteTile:
                    # remove tile from list
                    self.listManager.deleteTile(dropped.tile)
                    pass
                case _:
                    # Reset dropped tile to original position
                    pass

        self.redraw(self.pageFrame, self.listManager.getPageFirstTile(droppedIndex))



    def cont(self):
        """final function call"""
        self.pageFrameManager.finish()



    def submitEdit(self, pageTileIndex):
        """redraw after an edit is made
        
        Parameters
        ----------
        pageTileIndex : int
        """

        self.redraw(self.pageFrame, self.listManager.getPageFirstTile(pageTileIndex))



    def pageTileSetup(self, parent, tiles: list[PageTile]):
        """gives each tile it's parent frame, and binds listeners to each tile
        
        Parameters
        ----------
        parent : PageFrame
        tiles : PageTile[]
        """
        
        for tile in tiles:
            tile.setParent(parent)
            self.setMouseManager(tile)
            # self.mouseManager.addDraggable(tile)
            # self.mouseManager.addEditable(tile)

    

    def setMouseManager(self, tile):
        """adds mouse event listeners to the tile passed
        
        Parameters
        ----------
        tile : PageTile
        """
        self.mouseManager.addDraggable(tile)
        self.mouseManager.addEditable(tile)



