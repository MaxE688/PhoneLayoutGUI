import tkinter as tk

class EditTileFrame(tk.Toplevel):
    """
    window that opens when editing a tile

    Attributes
    ----------
    toplevel : tk.Toplevel
        Toplevel of the PageTile being edited
    tile : PageTile
        tile that is being edited
    typeLabel : tk.Label
        label widget for type field
    lineLabel : tk.Label
        label widget for line field
    valueLabel : tk.Label
        label widget for value field
    labelLabel : tk.Label
        label widget for label field
    clicked : tk.StringVar
        current selected option from OptionMenu
    typeDropMenu : tk.OptionsMenu
        OptionMenu widget for drop down menu
    lineBox : tk.Spinbox
        SpinBox widget for line field
    valueEntry : tk.Entry
        Entry widget for value field
    labelEntry : tk.Entry
        Entry widget for label field
    submitBtn : tk.Button
        submit button
    cancelBtn : tk.Button
        cancel button

    Methods
    -------
    setButtons(submit : tk.Button, cancel : tk.Button)
        create reference to to submit and cancel buttons
    getClicked()
        returns the currently selected option from OptionMenu
    getLineBox()
        returns line box's string
    getValueEntry()
        returns text entered by user
    getLabelEntry()
        returns text entered by user
    draw()
        draw widget on parent
    center()
        places the window in the center of the screen

    """

    def __init__(self, pageTile, options, currentOption):
        """
        Parameters
        ----------
        pageTile : PageTile
        options : str[]
        currentOption : str
        """
        super().__init__()
        self.toplevel = pageTile.winfo_toplevel()
        self.tile = pageTile.tile

        self.typeLabel = tk.Label(self, text = "Button Type: ")
        self.lineLabel = tk.Label(self, text = "Line: ")
        self.valueLabel = tk.Label(self, text = "Value: ")
        self.labelLabel = tk.Label(self, text = "Label: ")

        self.clicked = tk.StringVar()
        self.clicked.set(currentOption)

        self.typeDropMenu = tk.OptionMenu(self, self.clicked, *options)

        lineVal = tk.StringVar()
        self.lineBox = tk.Spinbox(self, textvariable = lineVal, from_ = 1, to = 25)
        lineVal.set(str(self.tile.line))

        self.valueEntry = tk.Entry(self)
        self.labelEntry = tk.Entry(self)

        self.valueEntry.insert(0, str(self.tile.value))
        self.labelEntry.insert(0, str(self.tile.label))



    def setButtons(self, submit, cancel):
        """set submit and cancel buttons
        
        Parameters
        ----------
        submit : tk.Button
        cancel : tk.Button
        """

        self.submitBtn = submit
        self.cancelBtn = cancel



    def getClicked(self):
        """return selected option for tile type"""

        return self.clicked.get()
    


    def getLineBox(self):
        """return selected line value"""

        return self.lineBox.get()
    


    def getValueEntry(self):
        """return value entered for value field"""

        return self.valueEntry.get()
    


    def getLabelEntry(self):
        """return value entered for label field"""

        return self.labelEntry.get()



    def draw(self):
        """draws all widgets to parent"""

        self.typeLabel.pack()
        self.typeDropMenu.pack()

        self.lineLabel.pack()
        self.lineBox.pack()

        self.valueLabel.pack()
        self.valueEntry.pack()

        self.labelLabel.pack()
        self.labelEntry.pack()

        self.submitBtn.pack()
        self.cancelBtn.pack()



    def center(self):
        """centers the window on the screen"""

        x = self.toplevel.winfo_rootx()
        y = self.toplevel.winfo_rooty()
        rHeight = self.toplevel.winfo_height()
        rWidth = self.toplevel.winfo_width()
        height = 300
        width=200
        geo = str(width) + "x" + str(height) + "+" + str(int(x + rWidth/2 - width/2)) + "+" + str(int(y + rHeight/2 - height/2))
        print(geo)
        self.geometry(geo)

        center = '+' + str(x) + '+' + str(y)
        self.geometry(center)


