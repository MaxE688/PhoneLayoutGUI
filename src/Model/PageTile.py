import tkinter as tk

class PageTile(tk.Label):
   """
   tkinter label that represents a tile
   
   Attributes
   ----------
   index : int
      the index the of the tile this PageTile represents in the main tile list
   tile : Tile
      the tile this PageTile represents
   label : tk.StringVar
      the text shown for PageTiles
   parent : PageFrame
      parent of the tk.Label

   Methods
   -------
   setParent(parent : PageFrame)
      sets the parent for tk.Label
   setIndex(index : int)
      sets the index attribute
   setTile(tile : Tile)
      set the tile attribute
   setLabel(label : str)
      set the label attribute
   updateValues(newIndex : int, newTile : Tile, newLabel : str)
      updates the values of the attributes passed as arguments

   """

   def __init__(self, index, tile):
      """
      Parameters
      ----------
      index : int
      tile : Tile
      """

      self.index = index
      self.tile = tile
      self.label = tk.StringVar()



   def setParent(self, parent):
      """sets the parent attribute
      
      Parameters
      ----------
      parent : PageFrame
      """

      super().__init__(
                           parent,
                           textvariable= self.label,
                           width = 10,
                           height = 4,
                           relief = tk.RAISED
                     )
      
      self.parent = parent
      self.setLabel(self.tile.label)



   def setIndex(self, index):
      """sets index attribute
      
      Parameters
      ----------
      index : int
      """

      self.index = index



   def setTile(self, tile):
      """sets index attribute
      
      Parameters
      ----------
      tile : Tile
      """

      self.tile = tile


   # TODO: is this needed?
   def setLabel(self, label):
      print("set label");
      self.label.set(label)



   def updateValues(self, newIndex, newTile, newLabel):
      """updates the values of index, tile, and label attribute
      
      Parameters
      ----------
      newIndex : int
      newTile : Tile
      newLabel : str
      """

      self.index = newIndex
      self.tile = newTile
      self.label.set(newLabel)