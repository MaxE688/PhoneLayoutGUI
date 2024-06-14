
import math
from Controller.PageFrameManager import PageFrameManager
from View.FooterFrame import FooterFrame
from View.PageFrame import PageFrame
from Model.constants import phoneModels
from Controller.InitTileConfig import *
from Controller.ListManager import ListManager

class TileFrameManager:

    def __init__(self, frameManager):

        self.frameManager = frameManager
        self.root = frameManager.root
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

        if self.model == "Astra 6737i":
            self.listManager.setTopTiles()

        if self.pageCount < 1: self.pageCount = 1

        self.pageContainer = PageFrameManager(self)
     
     

    def forget(self):
        self.pageContainer.forget()



    def generateResults(self):
        self.frameManager.generateResults(self.listManager)



    def calcTilesPerPage(self, pageCount, tilesPerPage):
        if pageCount > 1:
            return tilesPerPage - 1
        return tilesPerPage

