from Model.PageTile import PageTile

class MouseManager:
    """
    Controller that manages mouse events

    Attributes
    ----------
    pageLayout : PageLayout
        instance of controller that handles layout
    startX : int
        the first x coordinate of a mouse event
    startY : int
        the first y coordinate of a mouse event
    startCol : int
        the column of the widget with a mouse event
    startRow : int
        the row of the widget with a mouse event

    Methods
    -------
    addDraggable(tile : Tile)
        binds methods to Tile widget related to drag and drop
    addEditable(tile : Tile)
        binds methods to Tile widget related to editing tile's attributes
    edit(event : Event)
        edit method that is binded to tile widgets
    onStart(event : Event)
        left click listener for tiles
    onDrag(event : Event)
        drag listener for tiles
    onDrop(event : Event)
        drop listener for tiles

    """

    def __init__(self, pageLayout):
        """
        Parameters
        ----------
        pageLayout : PageLayout
        """
        self.pageLayout = pageLayout
        # self.tfm = tfManager



    def addDraggable(self, tile):
        """binds mouse listeners to the tile passed into it

        Parameters
        ----------
        tile : Tile
        """
        tile.bind("<ButtonPress-1>", self.onStart)
        tile.bind("<B1-Motion>", self.onDrag)
        tile.bind("<ButtonRelease-1>", self.onDrop)
        tile.configure(cursor="hand1")



    def addEditable(self, tile):
        """binds mouse listeners to the tile passed into it

        Parameters
        ----------
        tile : Tile
        """
        tile.bind("<Double-1>", self.edit)



    def edit(self, event):
        """calls editTile from pageLayout to pass the event's widget being edited

        Parameters
        ----------
        event : Event
        """
        self.pageLayout.editTile(event.widget)



    def onStart(self, event):
        """listener for left mouse click, captures mouse location
        
        Parameters
        ----------
        event : Event
        """

        widget = event.widget

        self.startX = event.x
        self.startY = event.y

        self.startCol = widget.grid_info()['column']
        self.startRow = widget.grid_info()['row']



    def onDrag(self, event):
        """listener for drag event
        
        Parameters
        ----------
        event : Event
        """

        widget = event.widget

        self.x = widget.winfo_x() - self.startX + event.x
        self.y = widget.winfo_y() - self.startY + event.y

        self.pageLayout.drag(widget, self.x, self.y)



    def onDrop(self, event):
        """listener for release mouse event
        
        Parameters
        ----------
        event : Event
        """

        widget: PageTile = event.widget

        x = widget.parent.winfo_rootx() + (widget.winfo_x() + event.x)
        y = widget.parent.winfo_rooty() + (widget.winfo_y() + event.y)
        
        print("x = widget.parent.winfo_rootx() + (widget.winfo_x() + event.x)")
        print("y = widget.parent.winfo_rooty() + (widget.winfo_y() + event.y)")
        print()
        print( str(x) + " = " + str(widget.parent.winfo_rootx()) + " + (" + str(widget.winfo_x()) + " + " + str(event.x) + ")")
        print( str(y) + " = " + str(widget.parent.winfo_rooty()) + " + (" + str(widget.winfo_y()) + " + " + str(event.y) + ")")

        self.pageLayout.drop(widget, x, y)


