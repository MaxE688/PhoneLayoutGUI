"""
TODO:
    - Add the rest of the forms for the tile information
"""



import tkinter as tk

# from Controller.TileData import TileData
# from tkinter import ttk

class EditTileFrame(tk.Tk):

    def __init__(self, editManager):
        # super().__init__()
        self.editManager = editManager
        self.tile = editManager.tile
        self.subRoot = tk.Toplevel(self.editManager.tfManager.root)

        self.subRoot.title("Edit Button Information")

        typeLabel = tk.Label(self.subRoot, text = "Button Type: ")
        lineLabel = tk.Label(self.subRoot, text = "Line: ")
        valueLabel = tk.Label(self.subRoot, text = "Value: ")
        labelLabel = tk.Label(self.subRoot, text = "Label: ")

        # editManager = TileData(tile, tfManager.model)
        dropOptions = self.editManager.getTypeOpts()

        self.clicked = tk.StringVar()
        self.clicked.set(self.editManager.getCurrOpt())

        typeDropMenu = tk.OptionMenu(self.subRoot, self.clicked, *dropOptions)


        lineVal = tk.StringVar()
        self.lineBox = tk.Spinbox(self.subRoot, textvariable = lineVal, from_ = 1, to = 25)
        lineVal.set(str(self.tile.line))

        self.valueEntry = tk.Entry(self.subRoot)
        self.labelEntry = tk.Entry(self.subRoot)

        self.valueEntry.insert(0, str(self.tile.value))
        self.labelEntry.insert(0, str(self.tile.label))

        submitBtn = tk.Button(self.subRoot, text = "Submit")
        submitBtn['command'] = self.submit

        cancelBtn = tk.Button(self.subRoot, text = "Cancel")
        cancelBtn['command'] = self.cancel


        typeLabel.pack()
        typeDropMenu.pack()

        lineLabel.pack()
        self.lineBox.pack()

        valueLabel.pack()
        self.valueEntry.pack()

        labelLabel.pack()
        self.labelEntry.pack()

        submitBtn.pack()
        cancelBtn.pack()



    def submit(self):
        self.editManager.updateTile(
                                    self.clicked.get(),
                                    self.lineBox.get(),
                                    self.valueEntry.get(),
                                    self.labelEntry.get()
                                )

        self.subRoot.destroy()

    def cancel(self):
        self.subRoot.destroy()
