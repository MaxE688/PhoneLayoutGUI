# import constants
import sys
import tkinter as tk

class Root(tk.Tk):
    """
    Root for the whole program

    Attributes
    ----------
    fm : FrameManager
        Main controller

    Methods
    -------
    center()
        centers self on screen
    createMenu(fm : FrameManager)
        creates menu bar
    newCfg()
        Go back to config window to set a new config string
    selectModel()
        go bakc to select model window to set a new model
    quit()
        exit program
    gridConfigure()
        configure grid
    """

    def __init__(self):
        super().__init__()


    
    def center(self):
        """Centers self on screen"""

        self.update()

        screenW = self.winfo_screenwidth()
        screenH = self.winfo_screenheight()
        width = self.winfo_width()
        height = self.winfo_height()

        x = int((screenW/2)-(width/2))
        y = int((screenH/2)-(height/2))

        center = '+' + str(x) + '+' + str(y)
        self.geometry(center)


 
    def createMenu(self, fm):
        """Creates the menu bar
        
        Parameters
        ----------
        fm : FrameManager
        """

        self.fm = fm

        menuBar = tk.Menu(fm.root)

        file = tk.Menu(menuBar, tearoff = 0)
        file.add_command(label = "New Config", command = self.newCfg)
        file.add_command(label = "Select Model", command = self.selectModel)
        file.add_separator()
        file.add_command(label = "Quit", command = self.quit)

        menuBar.add_cascade(label = "File", menu = file)

        fm.root.config(menu = menuBar)


    
    
    def newCfg(self):
        """Go back to window for user to enter new config text"""

        #self.fm.newConfigFrame(self.children['!frame'])
        self.fm.initConfigFrame(self.children['!frame'])



    def selectModel(self):
        """Go back to window for user to select phone model"""
        
        self.fm.initModelSelectFrame()



    def quit(self):
        """Exit application"""
        
        sys.exit(0)



    def gridConfigure(self):
        """Configure grid"""
        
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(1, weight = 1)


