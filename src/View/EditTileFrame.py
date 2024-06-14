"""
TODO:
    - Add the rest of the forms for the tile information
"""
import tkinter as tk

class EditTileFrame(tk.Toplevel):

    def __init__(self, pageTile, options, currentOptions):
        super().__init__()
        self.root = pageTile.winfo_toplevel()
        self.tile = pageTile.tile

        self.typeLabel = tk.Label(self, text = "Button Type: ")
        self.lineLabel = tk.Label(self, text = "Line: ")
        self.valueLabel = tk.Label(self, text = "Value: ")
        self.labelLabel = tk.Label(self, text = "Label: ")

        self.clicked = tk.StringVar()
        self.clicked.set(currentOptions)

        self.typeDropMenu = tk.OptionMenu(self, self.clicked, *options)

        lineVal = tk.StringVar()
        self.lineBox = tk.Spinbox(self, textvariable = lineVal, from_ = 1, to = 25)
        lineVal.set(str(self.tile.line))

        self.valueEntry = tk.Entry(self)
        self.labelEntry = tk.Entry(self)

        self.valueEntry.insert(0, str(self.tile.value))
        self.labelEntry.insert(0, str(self.tile.label))



    def setButtons(self, submit, cancel):
        self.submitBtn = submit
        self.cancelBtn = cancel



    def getClicked(self):
        return self.clicked.get()
    


    def getLineBox(self):
        return self.lineBox.get()
    


    def getValueEntry(self):
        return self.valueEntry.get()
    


    def getLabelEntry(self):
        return self.labelEntry.get()



    def draw(self):
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
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        rHeight = self.root.winfo_height()
        rWidth = self.root.winfo_width()
        height = 300
        width=200
        geo = str(width) + "x" + str(height) + "+" + str(int(x + rWidth/2 - width/2)) + "+" + str(int(y + rHeight/2 - height/2))
        print(geo)
        self.geometry(geo)

        center = '+' + str(x) + '+' + str(y)
        self.geometry(center)


