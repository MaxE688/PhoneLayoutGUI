from Model.constants import *
from View.Root import *
from View.ModelSelectFrame import *
from View.ConfigFrame import *
from View.ResultsFrame import ResultsFrame
from Controller.TileFrameManager import *
from Controller.ResultsGenerator import ResultsGenerator

class FrameManager:
    """
    Controller for managing all of the windows used throughout the process 

    Attributes
    ----------
    root : Root
        The window that contains frames
    modelSelectFrame : ModelSelectFrame
        instance of frame used for the model selection step
    configFrame : ConfigFrame
        instance of frame used for entering the button layout configuration being edited
    config : str
        the configuration string entered by user
    tileFrameManager : TileFrameManager
        instance of TileFrameManager controller
    resultsGenerator : ResultsGenerator
        instance of ResultsGenerator used to generate the final config string to be copied
    results : str
        final string generated for the user
    model : str
        model of the phone being edited
    brand : str
        brand of the phone being edited
    
    Methods
    -------
    initModelSelectFrame()
        initiates the Model Select Frame
    createWindow(frame : ttk.Frame)
        creates new Root used to contain Frames
    startLoop()
        starts the mainloop tkinter relies on
    setModel(model : str)
        sets model and brand attributes 
    initConfigFrame(frame : ttk.Frame, model : str)
        initiates the Config Frame
    generateResults(listManager : ListManager)
        generates the final string
    resultsFrame()
        creates the final frame used to display the results

    """

    def __init__(self):
        self.root = None

    
    def initModelSelectFrame(self):
        """Creates the window for user to select the model of phone"""

        self.root: Root = self.createWindow()
        self.modelSelectFrame = ModelSelectFrame(self)
        self.root.title(self.modelSelectFrame.title)
        self.root.center()


    # TODO: Should mainloop be restarted after root is destroyed
    #       If so, startLoop() call should come from this function, not Driver.py
    def createWindow(self, frame = None):
        """Creates new root 

        Parameters
        ----------
        frame : ttk.Frame | None
        """

        if frame != None:
            frame.destroy()
        if self.root != None:
            self.root.destroy()
        
        root = Root()
        return root



    def startLoop(self):
        """Starts the main loop"""

        self.root.mainloop()


    def setModel(self, model):
        """set model and brand attributes
        
        Parameters
        ----------
        model : str
        """

        self.model = model
        self.brand = phoneModels[model]['brand']



    def initConfigFrame(self, frame):
        """Creates the frame for user to paste button config
        
        Parameters
        ----------
        frame : ttk.Frame
        """

        self.root: Root = self.createWindow(frame)
        self.configFrame = ConfigFrame(self)
        self.root.title(self.configFrame.title)
        self.root.center()



    def initPhoneFrame(self, frame, configText):
        """Create the window for user to edit buttons
        
        Parameters
        ----------
        frame : ttk.frame
        configText : str
        """

        self.root: Root = self.createWindow(frame)
        self.config: str = configText
        self.tileFrameManager = TileFrameManager(self)
        self.root.title(self.tileFrameManager.title)
        self.root.createMenu(self)
        self.root.center()


    
    def generateResults(self, listManager):
        """Converts the button arrangement to text for final frame
        
        Parameters
        ----------
        listManager : ListManager
        """

        self.resultsGenerator = ResultsGenerator(listManager, self.model)
        self.results = self.resultsGenerator.getStrings()
        self.resultsFrame()


     
    def resultsFrame(self):
        """Creates window displaying the text output"""

        self.tileFrameManager.forget()
        self.resultsFrame = ResultsFrame(self.root, self.results)
