import math
from typing import List
from Model.PageTile import PageTile
from Model.constants import phoneModels


class ListManager:
  def __init__(self, tiles: List, model):
    self.tiles = tiles
    self.model = model
    self.tilesPerPage = phoneModels[model]["tilesPerPage"]
  


  def getTiles(self):
    return self.tiles
  


  def createPageTiles(self, startIndex, pageSize):
    tiles = []
    for i in range(pageSize):
      index = startIndex + i
      if index > len(self.tiles):
        break
      tiles.append(PageTile(index, self.tiles[index]))
    
    return tiles
  
  def getPageTiles(self, startIndex):
    tiles = []
    for i in range(self.getPageSize()):
      index = startIndex + i
      if index > len(self.tiles):
        break
      tiles.append(self.tiles[index])
    return tiles


  def shiftTile(self, tileIndex, destinationIndex):
    mTile = self.tiles.pop(tileIndex)
    self.tiles.insert(destinationIndex, mTile)
    for t in self.tiles:
      print(self.tiles.index(t))



  def getPageCount(self):

    return math.ceil(len(self.tiles) / self.getPageSize())
    # if self.model == "Astra 6737i":
    #   return math.ceil(len(self.tiles) / self.tilesPerPage)
   
    # if len(self.tiles) > self.tilesPerPage:
    #   return math.ceil(len(self.tiles)  / (self.tilesPerPage - 1))
      
    # return 1
  



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
  


  def getPageFirstTile(self, tileIndex):
    tilesPerPage = self.getPageSize()
    first = 0
    for t in self.tiles:
      index = self.tiles.index(t)
      mod = index % tilesPerPage

      if mod == 0:
        first = index
      if tileIndex == index:
        return first
    return first



  def addTile(self):
    print("Add Tile!")



  def test(self):
    print("Testing testing...")







