"""
ToDo:
    Root.py:
        - implement New Config option in Menu
        - Style:
            - SelectModelFrame
            - ConfigFrame
            - FooterFrame
            -

Note: Name of this file has changed from ChangeLayout.py


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



    def initModelSelectFrame(self, frame):
        self.root = self.createWindow(frame)
        self.modelSelectFrame = ModelSelectFrame(self)
        self.root.title(self.modelSelectFrame.title)
        self.root.center()



    def createWindow(self, frame):
        if frame != None:
            frame.destroy()
        if self.root != None:
            self.root.destroy()
        
        root = Root()
        return root



    def startLoop(self):
        self.root.mainloop()



    def initConfigFrame(self, frame, model):

        self.root = self.createWindow(frame)
        self.model = model
        self.brand = phoneModels[model]['brand']

        self.configFrame = ConfigFrame(self)
        self.root.title(self.configFrame.title)
        self.root.center()



    def initPhoneFrame(self, frame, configText):
        self.root = self.createWindow(frame)
        self.config = configText
        self.tileFrameManager = TileFrameManager(self)
        self.root.title(self.tileFrameManager.title)
        self.root.createMenu(self)
        self.root.center()



    def generateResults(self, listManager):
        self.resultsGenerator = ResultsGenerator(listManager.tiles, self.model)

        self.results = self.resultsGenerator.getStrings()

        self.resultsFrame()



    def resultsFrame(self):
        self.tileFrameManager.forget()

        self.resultsFrame = ResultsFrame(self.root, self.results)
