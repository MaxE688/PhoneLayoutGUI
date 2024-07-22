"""
ToDo:

    A37 Model Frame format breaks when the number of tiles change

"""
from Model.constants import *
from View.Root import *
from View.ModelSelectFrame import *
from View.ConfigFrame import *
from View.ResultsFrame import ResultsFrame
from Controller.TileFrameManager import *
from Controller.ResultsGenerator import ResultsGenerator

class FrameManager:

    def __init__(self):
        self.root = None


    # Creates the window for user to select the model of phone
    def initModelSelectFrame(self, frame):
        self.root: Root = self.createWindow(frame)
        self.modelSelectFrame = ModelSelectFrame(self)
        self.root.title(self.modelSelectFrame.title)
        self.root.center()


    # Creates new root 
    def createWindow(self, frame):
        if frame != None:
            frame.destroy()
        if self.root != None:
            self.root.destroy()
        
        root = Root()
        return root


    # Starts the main loop
    def startLoop(self):
        self.root.mainloop()


    # Creates the window for user to paste button config
    def initConfigFrame(self, frame, model):

        self.root: Root = self.createWindow(frame)
        self.model = model
        self.brand = phoneModels[model]['brand']

        self.configFrame = ConfigFrame(self)
        self.root.title(self.configFrame.title)
        self.root.center()


    # Create the window for user to edit buttons
    def initPhoneFrame(self, frame, configText):
        self.root: Root = self.createWindow(frame)
        self.config: str = configText
        self.tileFrameManager = TileFrameManager(self)
        self.root.title(self.tileFrameManager.title)
        self.root.createMenu(self)
        self.root.center()


    # Converts the button arrangement to text for final frame
    def generateResults(self, listManager):
        self.resultsGenerator = ResultsGenerator(listManager, self.model)
        self.results = self.resultsGenerator.getStrings()
        self.resultsFrame()


    # Creates window displaying the text output 
    def resultsFrame(self):
        self.tileFrameManager.forget()
        self.resultsFrame = ResultsFrame(self.root, self.results)
