from Controller import FrameManager
from Controller.PageFrameManager import PageFrameManager
from View.FooterFrame import FooterFrame
from View.PageFrame import PageFrame
from Model.constants import Model, phoneModels
from Controller.InitTileConfig import *
from Controller.ListManager import ListManager

#TODO: Rename this class 
class TileFrameManager:
    """create tile objects from config string, gives tile objects to list manager
    
    Attributes
    ----------
    frameManager : FrameManager
        instance of the main frame manager
    model : str
        model of the phone being edited
    currentPage : int
        number of the current page
    title : str
        title of the window
    listManager : ListManager
        controller that keeps track of operations performed on the list of tiles
    pageCount : int
        the number of pages that exist
    tilesPerPage : int
        the number of tiles each page can contain
    pageContainer : PageFrameManager
        instance of controller that ties phone's buttons frame and the footer frame

    Methods
    -------
    forget()
        forget instance of pageContainer
    generateResults()
        passes tile list to main controller to generate the final output config string
    calcTilePerPage(pageCount : int, tilesPerPage : int)
        returns the number of tiles that can fit on a single page

    """

    def __init__(self, frameManager):
        """
        Parameters
        ----------
        frameManager : FrameManager
        """

        self.frameManager: FrameManager = frameManager
        #self.root = frameManager.root
        self.model = frameManager.model
        cfg = frameManager.config
        self.currentPage = 0
        self.title = "Button Page: " + self.model

        parsedConfig = InitTileConfig(self.model, phoneModels[self.model]['brand'], cfg)
        
        configTiles = parsedConfig.getTiles()
        tilesPerPage = phoneModels[self.model]['tilesPerPage']
        self.listManager = ListManager(configTiles, self.model)
        self.pageCount = self.listManager.getPageCount() 
        self.tilesPerPage = self.calcTilesPerPage(self.pageCount, tilesPerPage)

        if self.model == Model.AASTRA_6737.value:
            self.listManager.setTopTiles()

        if self.pageCount < 1: self.pageCount = 1

        self.pageContainer = PageFrameManager(self)
     
     

    def forget(self):
        """forgets child frames"""
        
        self.pageContainer.forget()



    def generateResults(self):
        """passes list to main controller"""

        self.frameManager.generateResults(self.listManager)



    def calcTilesPerPage(self, pageCount, tilesPerPage):
        """returns the number os tiles a single page can hold
        
        Parameters
        ----------
        pageCount : int
        tilesPerPage : int
        """

        if pageCount > 1:
            return tilesPerPage - 1
        return tilesPerPage

