import math
from typing import List
from Model.PageTile import PageTile
from Model.constants import phoneModels
from Model.Tile import Tile


class ListManager:

  def __init__(self, tiles: List, model):
    self.tiles = tiles
    self.model = model
    self.tilesPerPage = phoneModels[model]["tilesPerPage"]
    


  def getTiles(self):
    return self.tiles
  


  def setTopTiles(self):
    self.topTiles = []
    for i, tile in enumerate(list(self.tiles)):
      if tile.id[:3] == "top":
        if self.tiles.count(tile) > 0:
          self.tiles.remove(tile)
        pTile = PageTile(i, tile)
        self.topTiles.append(pTile)    

    # for t in self.topTiles:
    #   if t.tile.id[:3] == "top" and self.tiles.count(t) > 0:
    #     self.tiles.remove(t)

    print()

  def getTopTiles(self):
    for i, tile in enumerate(self.topTiles):
      tile.updateValues(i, tile.tile, tile.tile.label)
    return self.topTiles



  def createPageTiles(self, startIndex, pageSize):
    tiles = []
    for i in range(pageSize):
      index = startIndex + i
      if index >= len(self.tiles):
        break
      tiles.append(PageTile(index, self.tiles[index]))
    
    return tiles


  
  def getPageTiles(self, startIndex):
    tiles = []
    for i in range(self.getPageSize()):
      index = startIndex + i
      if index >= len(self.tiles):
        break
      tiles.append(self.tiles[index])
    return tiles



  def getPageCount(self):

    tileCount = len(self.tiles)
    # if self.model == "Astra 6737i":
    #   tileCount -= 6

    num = math.ceil(tileCount / self.getPageSize())
    return num



  def getPageSize(self):
    tileCount = len(self.tiles)
    if tileCount > self.tilesPerPage and self.model != "Astra 6737i":
      return self.tilesPerPage - 1
    return self.tilesPerPage
  


  # mod each index by tilesPerPage
  # Each 0 is first element in page
  # return page number when index matches argument tileIndex
  def getPageOfIndex(self, tileIndex):
    tilesPerPage = self.getPageSize()
    page = 0
    for t in self.tiles:
      index = self.tiles.index(t)
      mod = index % tilesPerPage

      if mod == 0:
        page += 1
      if tileIndex == index:
        return page
    return page



  # Get the first PageTile on page containg tileIndex
  def getPageFirstTile(self, tileIndex):
    tilesPerPage = self.getPageSize()
    first = 0
    for index, t in enumerate(self.tiles):
      mod = index % tilesPerPage 

      if mod == 0:
        first = index
      if tileIndex == index:
        return first

    return first



  def shiftTile(self, tileIndex, destinationIndex):
    mTile = self.tiles.pop(tileIndex)
    self.tiles.insert(destinationIndex, mTile)
    


  def shiftTopTile(self, tileIndex, destinationIndex):
    mTile = self.topTiles.pop(tileIndex)
    self.topTiles.insert(destinationIndex, mTile)



  def toNextPage(self, droppedIndex, lastIndex):
    if lastIndex + 1 >= len(self.tiles):
      dropped = self.tiles.pop(droppedIndex)
      self.tiles.append(dropped)
    else:
      lastIndex += 1
      self.shiftTile(droppedIndex, lastIndex)



  def toPrevPage(self, droppedIndex, insertIndex):
    if insertIndex - 1 < 0:
      self.shiftTile(droppedIndex, 0)
    else:
      self.shiftTile(droppedIndex, insertIndex - 1)

      
    
  def deleteTile(self, tile):
    self.tiles.remove(tile)



  def addTile(self, tile):
    # newTile = Tile()
    self.tiles.append(tile)
    print("Add Tile!")



  def test(self):
    print("Testing testing...")
    for t in self.tiles:
      print(t.label)






