import math
from typing import List
from Model.PageTile import PageTile
from Model.constants import phoneModels
#from Model.Tile import Tile


class ListManager:
  """
  Controller for managing the list of tiles that will be used to generate output config string

  Attributes
  ----------
  tiles : Tiles[]
    list of all tiles to be added to output config string
  model : str
    model of the phone being edited
  tilesPerPage : int
    the number of buttons on a single page of the phone being edited
  topTiles : PageTile[]
    list of PageTiles that represent topsoftkeys for applicable  models 

  Methods
  -------
  getTiles()
    returns instance of list of Tiles
  setTopTiles()
    instanciate topTiles list to store topsoftkeys for applicable phone models
  getTopTiles()
    return list of top tiles
  createPageTiles(startIndex : int, pageSize : int)
    creates list of PageTiles 
  getPageTiles(startIndex : int)
    returns list of PageTiles
  getPageCount()
    returns the number of pages
  getPageSize()
    returns the number of tiles that a single page can hold
  getPageOfIndex(tileIndex : int)
    returns the page number that contains the tile at the index tileIndex
  getPageFirstTile(tileIndex : int)
    returns the index of the first tile on the same page as the tile at the index tileIndex
  shiftTile(tileIndex : int, destinationIndex : int)
    changes the location of the tile at the index tileIndex into the index destinationIndex
  shiftTopTIle(tileIndex : int, destinationIndex : int)
    changes the location of the tile at the index tileIndex into the index destinationIndex
  toNextPage(droppedIndex : int, lastIndex : int)
    moves the tile at the index droppedIndex to the next page on the phone
  toPrevPage(droppedIndex : int, insertIndex : int)
    moves the tile at the index droppedIndex to the previous page on the phone
  deleteTile(tile : Tile)
    removes the provided tile from the list
  addTile(tile : Tile)
    adds a new tile to the end of the list
  test()
    used to print the labels of the tiles in the list
  """

  def __init__(self, tiles: List, model):
    """
    Parameters
    ----------
    tiles : Tiles[]
    model : str
    """
    self.tiles = tiles
    self.model = model
    self.tilesPerPage = phoneModels[model]["tilesPerPage"]
    


  def getTiles(self):
    """returns the list of tiles"""
    return self.tiles
  


  def setTopTiles(self):
    """creates list of PageTiles for topsoftkeys"""
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
    """returns list of topsoftkeys"""
    for i, tile in enumerate(self.topTiles):
      tile.updateValues(i, tile.tile, tile.tile.label)
    return self.topTiles



  def createPageTiles(self, startIndex, pageSize):
    """creates list of PageTiles
    
    Parameters
    ----------
    startIndex : int
      index of the first tile in tiles on the page being displayed 
    pageSize : int
      the size of the page being displayed
    """
    tiles = []
    for i in range(pageSize):
      index = startIndex + i
      if index >= len(self.tiles):
        break
      tiles.append(PageTile(index, self.tiles[index]))
    
    return tiles


  
  def getPageTiles(self, startIndex):
    """returns list of tiles on the page being displayed
    
    Parameters
    ----------
    startIndex : int
      the first tile on the page being displayed 
    """
    tiles = []
    for i in range(self.getPageSize()):
      index = startIndex + i
      if index >= len(self.tiles):
        break
      tiles.append(self.tiles[index])
    return tiles



  def getPageCount(self):
    """returns the number of pages holding tiles"""

    tileCount = len(self.tiles)
    # if self.model == "Astra 6737i":
    #   tileCount -= 6

    num = math.ceil(tileCount / self.getPageSize())
    return num



  def getPageSize(self):
    """returns number of tiles that can fit on one page"""
    tileCount = len(self.tiles)
    if tileCount > self.tilesPerPage and self.model != "Astra 6737i":
      return self.tilesPerPage - 1
    return self.tilesPerPage
  


  # mod each index by tilesPerPage
  # Each 0 is first element in page
  # return page number when index matches argument tileIndex
  def getPageOfIndex(self, tileIndex):
    """returns the page that has the tile at the provided index
    
    Parameters
    ----------
    tileIndex : int
      index of the tile on the page being searched for
    """
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
    """returns the fisrt tile on the same page as the tile at the index provided
    
    Parameters
    ----------
    tileIndex : int 
      index of a tile
    """
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
    """change location of tile at provided index to the desitnation index
    
    Parameters
    ----------
    tileIndex : int
      index of the tile being moved
    destinationIndex : int
      the index where the tile will be placed
    """
    mTile = self.tiles.pop(tileIndex)
    self.tiles.insert(destinationIndex, mTile)
    


  def shiftTopTile(self, tileIndex, destinationIndex):
    """change location of the tile at the privided index to the destination index
    
    Parameters
    ----------
    tileIndex : int
      index of the tile being moved
    destinationIndex : int
      the index where the tile will be placed
    """
    mTile = self.topTiles.pop(tileIndex)
    self.topTiles.insert(destinationIndex, mTile)



  def toNextPage(self, droppedIndex, lastIndex):
    """places the tile at the index provided to the next page
    
    Paramters
    ---------
    droppedIndex : int
      the index of the tile being moved to the next page
    lastIndex : int
      the last index on the of the page that has the tile being moved
    """
    if lastIndex + 1 >= len(self.tiles):
      dropped = self.tiles.pop(droppedIndex)
      self.tiles.append(dropped)
    else:
      lastIndex += 1
      self.shiftTile(droppedIndex, lastIndex)



  def toPrevPage(self, droppedIndex, insertIndex):
    """places the tile at the index provided to the previous page
    
    Paramters
    ---------
    droppedIndex : int
      index of the tile being moved to the previous page
    insertIndex : int
      the index the tile being moved will be moved to
    """
    if insertIndex - 1 < 0:
      self.shiftTile(droppedIndex, 0)
    else:
      self.shiftTile(droppedIndex, insertIndex - 1)

      
    
  def deleteTile(self, tile):
    """delete tile from list"""
    self.tiles.remove(tile)



  def addTile(self, tile):
    """add new tile to the end of the list"""
    # newTile = Tile()
    self.tiles.append(tile)
    print("Add Tile!")



  def test(self):
    print("Testing testing...")
    for t in self.tiles:
      print(t.label)






