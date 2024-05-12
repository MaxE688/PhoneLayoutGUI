# from View.EditTileFrame import EditTileFrame
# from View.ModelFrame import ModelFrame

class MouseManager:

    def __init__(self, modelFrame, tfManager):
        self.modelFrame = modelFrame
        self.tfm = tfManager

    def addDraggable(self, tile):
        tile.bind("<ButtonPress-1>", self.onStart)
        tile.bind("<B1-Motion>", self.onDrag)
        tile.bind("<ButtonRelease-1>", self.onDrop)
        tile.configure(cursor="hand1")

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

        self.modelFrame.drag(widget, self.x, self.y)

    def onDrop(self, event):

        widget = event.widget

        x = self.modelFrame.winfo_rootx() + (widget.winfo_x() + event.x)
        y = self.modelFrame.winfo_rooty() + (widget.winfo_y() + event.y)

        self.modelFrame.drop(widget, x, y, self.startCol, self.startRow)


    def addEditable(self, tile):
        tile.bind("<Double-1>", self.edit)

    def edit(self, event):
        self.modelFrame.editTile(event.widget)
        print("Edit me!")
