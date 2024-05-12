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
# import Controller.TileFrameManager
from Controller.TileFrameManager import *
from Controller.ResultsGenerator import ResultsGenerator
# from Controller.InitTileConfig import *

class FrameManager:

    def __init__(self):
        self.root = None

    def generateResults(self, tileList):
        print("GR here")
        self.rg = ResultsGenerator(tileList, self.brand)

        self.results = self.rg.getStrings()
        self.resultsFrame()


    def resultsFrame(self):
        print("forget mainFrame")
        self.tfm.forget()

        self.resultFrame = ResultsFrame(self.root, self.results)


    #ToDo Change name of this method
    def mainFrame(self, cfg):
        self.cfg = cfg
        self.root = self.createWindow(self.cfgFrame)
        # self.root.center()

        self.tfm = TileFrameManager(self, self.root, self.model, self.cfg)
        self.tfm.create()
        self.root.title(self.tfm.title)
        self.root.createMenu(self)
        self.root.center()


    def configFrame(self, frame, model):

        self.model = model
        self.brand = phoneModels[model]['brand']

        self.root = self.createWindow(frame)
        # self.root.center()
        # self.root.setSize(500,800)
        self.cfgFrame = ConfigFrame(self)
        self.root.title(self.cfgFrame.title)
        self.root.center()

    def selectModelFrame(self, frame):

        self.root = self.createWindow(frame)
        # self.root.center()

        # self.root.setSize(SELECT_MODEL_FRAME_WIDTH, SELECT_MODEL_FRAME_HEIGHT)
        self.msFrame =  ModelSelectFrame(self)
        self.root.title(self.msFrame.title)
        self.root.center()


    def createWindow(self, frame):
        if frame != None:
            frame.destroy()
        if self.root != None:
            self.root.destroy()
        root = Root()
        # root.center()

        return root

    def startLoop(self):
        self.root.mainloop()

    # def getPhoneModels(self):
    #     return phoneModels







# fm = FrameManager()
# fm.selectModelFrame(None)
# fm.startLoop()
