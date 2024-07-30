
from tkinter import ttk
from Controller.PageLayout import PageLayout
from View.FooterFrame import FooterFrame

class PageFrameManager:
    """
    Controller that mangages PageFrames. Ties the footer frame and the page frame together

    Attributes
    ----------
    tileFrameManager : TileFrameManager
        instance of TileFrameManager
    listManager : ListManager
        instance of list manager
    containerFrame : ttk.Frame
        frame used to hold pageLayout frame and footer frame
    pageLayout : PageLayout
        controller for the Page frame holding tiles
    footerFrame : FooterFrame
        footer frame to give control to the page frames


    Methods
    -------
    updatePageLabel(currentPage : int, totalPages : int)
        changes the page number label to show current page
    finish()
        after user submits  their edits
    forget()
        forget container frame
    """

    def __init__(self, tileFrameManager):
        """
        Parameters
        ----------
        tileFrameManager : TileFrameManager
        """
        
        self.tileFrameManager = tileFrameManager

        self.listManager = tileFrameManager.listManager
        #TODO: set minimum sizes
        self.containerFrame = ttk.Frame(tileFrameManager.root)
        self.pageLayout = PageLayout(self, self.containerFrame, tileFrameManager.model, self.listManager)
        self.footerFrame = FooterFrame(self.containerFrame, self.listManager, self.pageLayout) 

        self.containerFrame.pack()



    def updatePageLabel(self, currentPage, totalPages):
        """updates page number to reflect current page
        
        Parameters
        ----------
        currentPage : int
        totalPages : int
        """
        self.footerFrame.setPageLabel(currentPage, totalPages)



    def finish(self):
        """PageFrameManager is finished, and it's time to generate results"""
        self.tileFrameManager.generateResults()



    def forget(self):
        """forget self"""
        self.containerFrame.pack_forget()


