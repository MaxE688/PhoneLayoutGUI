
import math
from View.ParentModelFrame import ParentModelFrame
from View.FooterFrame import FooterFrame
from View.ModelFrame import ModelFrame
from Model.constants import phoneModels
from Controller.InitTileConfig import *

class TileFrameManager:
# class TileFrameManager(ttk.Frame):
    def __init__(self, frameManager, root, model, cfg):

        self.frameManager = frameManager
        self.root = root
        self.model = model
        self.currentPage = 0
        self.title = "Button Page: " + self.model

        parsedConfig = InitTileConfig(phoneModels[model]['brand'], cfg)
        configTiles = parsedConfig.getTiles()

        tilesPerPage = phoneModels[model]['tilesPerPage']
        if len(configTiles) > tilesPerPage:
            tilesPerPage -= 1

        self.pageCount = math.ceil(len(configTiles) / tilesPerPage)

        if self.pageCount < 1: self.pageCount = 1

        self.pageContainer = ParentModelFrame(self.root)
        self.footerFrame = FooterFrame(self)


        self.tilePageFrames = []
        # x = 0
        # for i in range(self.pageCount):
        #     if self.pageCount > 1:
        #         tiles = configTiles[x : x + tilesPerPage ]
        #     else:
        #         tiles = configTiles
        #     page = ModelFrame(self, tiles)
        #     page.makeDragable()
        #     page.makeEditable()
        #     self.tilePageFrames.append(page)
        #     x += tilesPerPage
        if self.model == 'Astra 6737i':
            self.makePages6737(configTiles, tilesPerPage)
        else:
            self.makePages(configTiles, tilesPerPage)










    def makePages6737(self, configTiles, tilesPerPage):
        tiles = []
        topKeys = []
        cTiles = configTiles

        for tile in configTiles:
            # print(tile.id)
            if tile.id[0:3] == 'top':
                t = tile
                topKeys.append(t)
        for tile in topKeys:
            cTiles.remove(tile)


        if len(cTiles) > 6:
            tilesPerPage = 5

        print()
        print("cTiles: " + str(len(cTiles)))
        print("tilesPerPage: " + str(tilesPerPage))


        self.pageCount = math.ceil(len(cTiles) / tilesPerPage)

        print("PageCount: " + str(self.pageCount))
        print()

        tiles.extend(topKeys)
        x = 0
        for i in range(self.pageCount):
            if self.pageCount > 1:
                tiles.extend(cTiles[x : x + tilesPerPage])
            else:
                tiles.extend(cTiles)
            page = ModelFrame(self, tiles)
            page.makeDragable()
            page.makeEditable()
            self.tilePageFrames.append(page)
            x += tilesPerPage
        print()
        for page in self.tilePageFrames:
            for tile in page.tiles:
                print(tile.id)
        print()






    # currently takes full list of tiles, and divides them into individual pages
    # when a change occurs to one of the pages, the tiles are trying to adjust
    # based on their current page.

    # Consider managing the full list here, and when a tile is moved/deleted/created
    # delete all current pages, and recreate them with this function


    def makePages(self, cTiles, tilesPerPage):
        x = 0
        for i in range(self.pageCount):
            if self.pageCount > 1:
                tiles = cTiles[x : x + tilesPerPage]
            else:
                tiles = cTiles
            page = ModelFrame(self, tiles)
            page.makeDragable()
            page.makeEditable()
            self.tilePageFrames.append(page)
            x += tilesPerPage




































    def create(self):
        print("Creating Tile Frame")
        self.root.gridConfigure()
        self.pageContainer.create(self.tilePageFrames)
        self.footerFrame.create()
        # self.root.center()

    def forget(self):
        self.pageContainer.grid_forget()
        self.footerFrame.grid_forget()


    def nextPage(self):
        print("Page Count: " + str(self.pageCount))
        print("Current Page before: " + str(self.currentPage))
        print("Next Page before: " + str(self.currentPage + 1))

        curr = self.currentPage % self.pageCount
        next = (self.currentPage + 1) % self.pageCount
        self.pageContainer.nextPage(curr, next)
        # self.currentPage += 1
        self.currentPage = next
        self.footerFrame.updateLabel(next)

        print("Current Page after: " + str(self.currentPage))
        print("Next Page after: " + str(next))

    def prevPage(self):
        print("Page Count: " + str(self.pageCount))
        print("Current Page before: " + str(self.currentPage))
        print("Next Page before: " + str(self.currentPage + 1))


        curr = self.currentPage % self.pageCount
        prev = (self.currentPage - 1) % self.pageCount
        self.pageContainer.prevPage(curr, prev)
        # self.currentPage -= 1
        self.currentPage = prev
        self.footerFrame.updateLabel(prev)

        print("Current Page after: " + str(curr))
        print("Next Page after: " + str(next))

    def toNextPage(self, page, tile):
        nPage = (self.tilePageFrames.index(page) + 1) % len(self.tilePageFrames)
        if self.isSecondPageLast(page):
            copyTile = page.layoutManger.copyTile(self.tilePageFrames[0], page.tiles[0])
            self.tilePageFrames[nPage].tiles.append(copyTile)
            return None
        else:
            swappedTile = self.tilePageFrames[nPage].swapTilesNext(tile)
            return swappedTile

    def toPrevPage(self, page, tile):
        pPage = (self.tilePageFrames.index(page) - 1) % len(self.tilePageFrames)
        if self.isSecondPageLast(page):
            copyTile = page.layoutManager.copyTile(self.tilePageFrames[0], page.tiles[0])
            self.tilePageFrames[pPage].tiles.append(copyTile)
            return None
        else:
            swappedTile = self.tilePageFrames[pPage].swapTilesPrev(tile)
            return swappedTile


    def isSecondPageLast(self, page):
        if self.pageCount == 2 and page == self.tilePageFrames[-1]:
            if len(page.tiles) == 1:
                return True

        return False

    def addTileShift(self, page, tile, tilesPerPage):
        #if you're here it means page is full
        if page == self.tilePageFrames[-1]:
            #create new page for last tile
            tiles = []
            newPage = ModelFrame(self, tiles)

            newTile = page.layoutManager.copyTile(newPage, tile)

            newPage.tiles.append(newTile)

            if self.pageCount == 1:
                lastTile = page.tiles.pop()
                copyTile = page.layoutManager.copyTile(newPage, lastTile)
                newPage.tiles.insert(0, copyTile)

            newPage.makeDragable()
            newPage.makeEditable()

            self.tilePageFrames.append(newPage)
            self.pageCount = len(self.tilePageFrames)
            self.footerFrame.updateLabel(self.currentPage)


        else:
            pageIndex = self.tilePageFrames.index(page) + 1
            nextPage = self.tilePageFrames[pageIndex]

            newTile = nextPage.layoutManager.copyTile(nextPage, tile)

            nextPage.tiles.insert(0, newTile)

            if len(nextPage.tiles) > tilesPerPage:
                lastTile = nextPage.tiles.pop()
                self.addTileShift(nextPage, lastTile, tilesPerPage)
        for p in self.tilePageFrames:
            p.redraw()


    def deleteTileShift(self, page):
        if page != self.tilePageFrames[-1]:
            nextPage = self.tilePageFrames[self.tilePageFrames.index(page) + 1]
            firstTile = nextPage.tiles.pop(0)

            backTile = nextPage.layoutManager.copyTile(page, firstTile)
            page.tiles.append(backTile)

            self.deleteTileShift(nextPage)
        else:
            if len(page.tiles) == 0:
                self.deletePage(page)

        for p in self.tilePageFrames:
            p.redraw()


    def deletePage(self, page):
        if page == self.tilePageFrames[self.currentPage]:
            self.prevPage()
        self.tilePageFrames.remove(page)
        page.destroy()
        self.pageCount = len(self.tilePageFrames)
        if self.pageCount == 1:
            self.tilePageFrames[self.currentPage].redraw()

        self.footerFrame.updateLabel(self.currentPage)

    def cont(self):
        print("TFM cont...")
        exportTileList = self.makeTileList(self.tilePageFrames)
        self.frameManager.generateResults(exportTileList)


    def makeTileList(self, pages):
        exportList = []
        for page in pages:
            exportList.extend(page.tiles)

        return exportList

    def setID(self):

        if phoneModels[self.model]['brand'] == "Astra":
            if self.model == 'Astra 6737i':
                self.set6737ID()
            else:
                self.setAstraID()
        elif phoneModels[self.model]['brand'] == "Yealink":
            self.setYealinkID()



    def set6737ID(self):

        topkey = 1
        softkey  = 1

        for page in self.tilePageFrames:
            for tile in page.tiles:
                print(tile.grid_info()['row'])
                if tile.grid_info()['row'] < 3:
                    tile.id = 'topsoftkey' + str(topkey)
                    topkey += 1
                else:
                    tile.id = 'softkey' + str(softkey)
                    softkey += 1


    def setAstraID(self):
        key = 1
        for page in self.tilePageFrames:
            for tile in page.tiles:
                tile.id = 'softkey' + str(key)
                key += 1

    def setYealinkID(self):
        key = 1
        for page in self.tilePageFrames:
            for tile in page.tiles:
                tile.id = "linekey." + str(key)
                key += 1
