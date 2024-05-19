# from View.EditTileFrame import EditTileFrame
# from View.ModelFrame import ModelFrame
import tkinter as tk

from Model.PageTile import PageTile

class MouseManager:

    def __init__(self, pageLayout):
        self.pageLayout = pageLayout
        # self.tfm = tfManager

    def addDraggable(self, tile):
        tile.bind("<ButtonPress-1>", self.onStart)
        tile.bind("<B1-Motion>", self.onDrag)
        tile.bind("<ButtonRelease-1>", self.onDrop)
        tile.configure(cursor="hand1")



    def addEditable(self, tile):
        tile.bind("<Double-1>", self.edit)

    def edit(self, event):
        self.pageLayout.editTile(event.widget)
        print("Edit me!")



    def onStart(self, event):
        print("button press")
        widget = event.widget

        self.startX = event.x
        self.startY = event.y

        self.startCol = widget.grid_info()['column']
        self.startRow = widget.grid_info()['row']


    def onDrag(self, event):

        widget = event.widget

        self.x = widget.winfo_x() - self.startX + event.x
        self.y = widget.winfo_y() - self.startY + event.y

        self.pageLayout.drag(widget, self.x, self.y)

    def onDrop(self, event):

        widget: PageTile = event.widget


        # x = self.pageLayout.winfo_rootx() + (widget.winfo_x() + event.x)
        # y = self.pageLayout.winfo_rooty() + (widget.winfo_y() + event.y)

        x = widget.parent.winfo_rootx() + (widget.winfo_x() + event.x)
        y = widget.parent.winfo_rooty() + (widget.winfo_y() + event.y)
        
        
        # print("Parent.rootX: " + str(widget.parent.winfo_rootx()))
        # print("Parent.rootY: " + str(widget.parent.winfo_rooty()))
        # print()
        # print("widget.rootX: " + str(widget.winfo_rootx()))
        # print("widget.rootY: " + str(widget.winfo_rooty()))
        # print()
        # print("x: " + str(x))
        # print("y: " + str(y))
        print("x = widget.parent.winfo_rootx() + (widget.winfo_x() + event.x)")
        print("y = widget.parent.winfo_rooty() + (widget.winfo_y() + event.y)")
        print()
        print( str(x) + " = " + str(widget.parent.winfo_rootx()) + " + (" + str(widget.winfo_x()) + " + " + str(event.x) + ")")
        print( str(y) + " = " + str(widget.parent.winfo_rooty()) + " + (" + str(widget.winfo_y()) + " + " + str(event.y) + ")")





        self.pageLayout.drop(widget, x, y, self.startCol, self.startRow)


