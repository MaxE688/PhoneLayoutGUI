"""
TODO:
    - Add the rest of the forms for the tile information
"""



import tkinter as tk

# from Controller.TileData import TileData
# from tkinter import ttk

class EditTileFrame(tk.Toplevel):

    # def __init__(self, editManager):
    def __init__(self, pageTile, options, currentOptions):
        super().__init__()
        self.root = pageTile.winfo_toplevel()
        self.tile = pageTile.tile
        # self.root = editManager.tfManager.root
        # self.editManager = editManager
        # self.tile = editManager.tile


        # self.subRoot = tk.Toplevel(self.root)
        # self.center(root)

        # self.subRoot.title("Edit Button Information")


        # typeLabel = tk.Label(self.subRoot, text = "Button Type: ")
        # lineLabel = tk.Label(self.subRoot, text = "Line: ")
        # valueLabel = tk.Label(self.subRoot, text = "Value: ")
        # labelLabel = tk.Label(self.subRoot, text = "Label: ")
        self.typeLabel = tk.Label(self, text = "Button Type: ")
        self.lineLabel = tk.Label(self, text = "Line: ")
        self.valueLabel = tk.Label(self, text = "Value: ")
        self.labelLabel = tk.Label(self, text = "Label: ")

        # editManager = TileData(tile, tfManager.model)
        # dropOptions = self.editManager.getTypeOpts()

        self.clicked = tk.StringVar()
        self.clicked.set(currentOptions)

        # typeDropMenu = tk.OptionMenu(self.subRoot, self.clicked, *dropOptions)
        # typeDropMenu = tk.OptionMenu(self, self.clicked, *dropOptions)
        self.typeDropMenu = tk.OptionMenu(self, self.clicked, *options)

        
        lineVal = tk.StringVar()
        # self.lineBox = tk.Spinbox(self.subRoot, textvariable = lineVal, from_ = 1, to = 25)
        self.lineBox = tk.Spinbox(self, textvariable = lineVal, from_ = 1, to = 25)
        lineVal.set(str(self.tile.line))

        # self.valueEntry = tk.Entry(self.subRoot)
        # self.labelEntry = tk.Entry(self.subRoot)
        self.valueEntry = tk.Entry(self)
        self.labelEntry = tk.Entry(self)

        self.valueEntry.insert(0, str(self.tile.value))
        self.labelEntry.insert(0, str(self.tile.label))

        # self.submitBtn = submitBtn
        # self.cancelBtn = cancelBtn

        # # submitBtn = tk.Button(self.subRoot, text = "Submit")
        # submitBtn = tk.Button(self, text = "Submit")
        # submitBtn['command'] = self.submit

        # # cancelBtn = tk.Button(self.subRoot, text = "Cancel")
        # cancelBtn = tk.Button(self, text = "Cancel")
        # cancelBtn['command'] = self.cancel


        # typeLabel.pack()
        # typeDropMenu.pack()

        # lineLabel.pack()
        # self.lineBox.pack()

        # valueLabel.pack()
        # self.valueEntry.pack()

        # labelLabel.pack()
        # self.labelEntry.pack()

        # submitBtn.pack()
        # cancelBtn.pack()
        # self.mainloop()

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
        # self.update()
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        rHeight = self.root.winfo_height()
        rWidth = self.root.winfo_width()
        # height = self.winfo_height()
        # width = self.winfo_width()
        height = 300
        width=200
        # geo = "+%d+%d" % (x,y+(height*2))
        # geo = "+" + str(x + rWidth/2 - width/2) + "+" + str(y + rHeight/2 - height/2)
        geo = str(width) + "x" + str(height) + "+" + str(int(x + rWidth/2 - width/2)) + "+" + str(int(y + rHeight/2 - height/2))
        print(geo)
        self.geometry(geo)

        # self.update()
        # screenW = self.winfo_screenwidth()
        # screenH = self.winfo_screenheight()
        # width = self.winfo_width()
        # height = self.winfo_height()
        #
        # x = int((screenW/2)-(width/2))
        # y = int((screenH/2)-(height/2))


        center = '+' + str(x) + '+' + str(y)
        self.geometry(center)


    # def submit(self):
    #     self.editManager.updateTile(
    #                                 self.clicked.get(),
    #                                 self.lineBox.get(),
    #                                 self.valueEntry.get(),
    #                                 self.labelEntry.get()
    #                             )
    #     # self.tile.i

    #     # self.subRoot.destroy()
    #     self.destroy()

    # def cancel(self):
    #     # self.subRoot.destroy()
    #     self.destroy()

