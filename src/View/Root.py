# import constants
import sys
import tkinter as tk

class Root(tk.Tk):

    def __init__(self):
        super().__init__()


    # Centers self on screen
    def center(self):
        self.update()

        screenW = self.winfo_screenwidth()
        screenH = self.winfo_screenheight()
        width = self.winfo_width()
        height = self.winfo_height()

        x = int((screenW/2)-(width/2))
        y = int((screenH/2)-(height/2))

        center = '+' + str(x) + '+' + str(y)
        self.geometry(center)


    # Creates the menu bar 
    def createMenu(self, fm):

        self.fm = fm

        menuBar = tk.Menu(fm.root)

        file = tk.Menu(menuBar, tearoff = 0)
        file.add_command(label = "New Config", command = self.newCfg)
        file.add_command(label = "Select Model", command = self.selectModel)
        file.add_separator()
        file.add_command(label = "Quit", command = self.quit)

        menuBar.add_cascade(label = "File", menu = file)

        fm.root.config(menu = menuBar)


    
    # Go back to window for user to enter new config text
    def newCfg(self):
        self.fm.newConfigFrame(self.children['!frame'])



    # Go back to window for user to select phone model
    def selectModel(self):
        self.fm.initModelSelectFrame(None)


    # Exit application
    def quit(self):
        sys.exit(0)


    # Configure grid
    def gridConfigure(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(1, weight = 1)


