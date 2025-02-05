import sys
import tkinter as tk
from tkinter import ttk
from Model.constants import phoneModels

class ModelSelectFrame(ttk.Frame):
    """
    Frame used to prompt user for the model they would like to edit

    Attributes
    ----------
    fm : FrameManager
        instance of main controller
    title : str
        title of window
    clicked : tk.StringVar
        keeps track of the option the user has selected

    Methods
    -------
    submit()
        submit phone model, and continue to next window
    cancel()
        exit program


    """

    def __init__(self, fm):
        """
        Parameters
        ----------
        fm : FrameManager
        """

        super().__init__(fm.root)

        self.fm = fm

        self.title = "Change Phone Layout: Select Model"

        self.pack()

        label1 = tk.Label(self, text = "Please select the model of phone:")
        label1.grid(column = 1, row = 0, columnspan = 2)

        dropOptions = list(phoneModels)

        self.clicked = tk.StringVar()
        self.clicked.set(dropOptions[0])

        dropMenu = tk.OptionMenu(self, self.clicked, *dropOptions)
        dropMenu.grid(column = 1, row = 1, columnspan = 2)

        submitBtn = tk.Button(self, text = "Submit")
        submitBtn['command'] = self.submit

        cancelBtn = tk.Button(self, text = "Cancel")
        cancelBtn['command'] = self.cancel

        submitBtn.grid(column = 4, row = 3)
        cancelBtn.grid(column = 5, row = 3)

        tk.Frame(self, height = 15, width = 100).grid(column = 0, row = 4)
        tk.Frame(self, width = 20).grid(column = 6, row = 4)



    def submit(self):
        """Event listener for submit button"""

        print(phoneModels[self.clicked.get()])
        self.fm.setModel(self.clicked.get())
        self.fm.initConfigFrame(self)



    def cancel(self):
        """Event listener for cancel button"""

        print('cancel')
        sys.exit(0)
