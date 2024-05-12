# import constants
import sys
import Model.constants
import tkinter as tk
# from constants import *
from tkinter import ttk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.center()

    def center(self):
        self.update()
        # print(self.winfo_screenwidth())
        # print(self.winfo_screenheight())
        # print(self.winfo_width())
        # print(self.winfo_height())
        # print()
        screenW = self.winfo_screenwidth()
        screenH = self.winfo_screenheight()
        width = self.winfo_width()
        height = self.winfo_height()

        x = int((screenW/2)-(width/2))
        y = int((screenH/2)-(height/2))


        center = '+' + str(x) + '+' + str(y)
        self.geometry(center)
        print('I am called from ROOT.CENTER')

    def createMenu(self, fm):

        self.fm = fm

        menuBar = tk.Menu(fm.root)

        file = tk.Menu(menuBar, tearoff = 0)
        file.add_command(label = "New Config", command = self.newCfg)
        file.add_command(label = "Select Model", command = self.selectModel)
        # file.add_command(label = "", command = )
        file.add_separator()
        file.add_command(label = "Quit", command = self.quit)

        menuBar.add_cascade(label = "File", menu = file)

        fm.root.config(menu = menuBar)

    def newCfg(self):
        print("Creating new configuration...")
        self.fm.configFrame(None, self.fm.model)
    def selectModel(self):
        self.fm.selectModelFrame(None)


    def gridConfigure(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(1, weight = 1)


    def quit(self):
        sys.exit(0)
