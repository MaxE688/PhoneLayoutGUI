import tkinter as tk
from tkinter import StringVar, ttk

class PageTile(tk.Label):
   def __init__(self, index, tile):
      self.index = index
      self.tile = tile
      self.label = StringVar()

   def setParent(self, parent):
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
      self.index = index

   def setTile(self, tile):
      self.tile = tile

   def setLabel(self, label):
      self.label.set(label)

   def updateValues(self, newIndex, newTile, newLabel):
      self.index = newIndex
      self.tile = newTile
      self.label.set(newLabel)