import tkinter as tk


class Tile:
    # def __init__(self, container, id, type, line, value, label):
    def __init__(self, id, type, line, value, label):
        self.id = id
        self.type = type
        if line == None:
            self.line = None
        else:
            self.line = line
        self.label = label
        if value != None:
            self.value = value
        else:
            self.value = 0

        # self.tileText = tk.StringVar()
        # self.tileText.set(self.label)

        # self.tileText.trace('w', self.updateText)

    # def setParent(self, parent):


    #     super().__init__(
    #                         parent,
    #                         textvariable = self.tileText,
    #                         width = 10,
    #                         height = 4,
    #                         relief = tk.RAISED
    #                     )

    # def updateText(self, *args):
    #     print("Change from Tile.py Line: 36")
    #     self['text'] = self.tileText.get()



    def toString(self):
        return "id: " + str(self.id) + "\ntype: " + str(self.type) + "\nline: " + str(self.line) + "\nlabel: " + str(self.label) + "\nvalue: " + str(self.value) + "\n"
