import sys
import tkinter as tk

from tkinter import ttk
from Model.constants import phoneModels

class ModelSelectFrame(ttk.Frame):

    def __init__(self, fm):
        super().__init__(fm.root)

        self.fm = fm

        self.title = "Change Phone Layout: Select Model"

        # self['padx'] = 200
        # self['pady'] = 15
        # padOptions = {'padx':20, 'pady':15}
        # self.grid(column=0, row=0, **padOptions)
        self.pack()

        label1 = tk.Label(self, text = "Please select the model of phone:")
        label1.grid(column = 1, row = 0, columnspan = 2)

        # dropOptions = phoneModels.keys()
        dropOptions = list(phoneModels)

        self.clicked = tk.StringVar()
        # self.clicked.set("Astra 6737i")
        self.clicked.set(dropOptions[0])

        # dropMenu = tk.OptionMenu(self, self.clicked, *dropOptions)
        dropMenu = tk.OptionMenu(self, self.clicked, *dropOptions)
        dropMenu.grid(column = 1, row = 1, columnspan = 2)

        # tk.Frame(self, height = 300, width = 100).grid(column = 1, row = 1, columnspan = 2, rowspan = 5)
        # tk.Frame(self, height = 25, width = 350).grid(column = 3, row = 3, columnspan = 4)

        submitBtn = tk.Button(self, text = "Submit")
        submitBtn['command'] = self.submit
        cancelBtn = tk.Button(self, text = "Cancel")
        cancelBtn['command'] = self.cancel

        submitBtn.grid(column = 4, row = 3)
        cancelBtn.grid(column = 5, row = 3)

        tk.Frame(self, height = 15, width = 100).grid(column = 0, row = 4)
        tk.Frame(self, width = 20).grid(column = 6, row = 4)


    def submit(self):
        print(phoneModels[self.clicked.get()])
        self.fm.initConfigFrame(self, self.clicked.get())

    def cancel(self):
        print('cancel')
        sys.exit(0)
