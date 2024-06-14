
from tkinter import ttk
from Controller.PageLayout import PageLayout
from View.FooterFrame import FooterFrame

class PageFrameManager:

    def __init__(self, tileFrameManager):
        self.tileFrameManager = tileFrameManager

        self.listManager = tileFrameManager.listManager
        self.containerFrame = ttk.Frame(tileFrameManager.root)
        self.pageLayout = PageLayout(self, self.containerFrame, tileFrameManager.model, self.listManager)
        self.footerFrame = FooterFrame(self.containerFrame, self.listManager, self.pageLayout) 

        self.containerFrame.pack()



    def updatePageLabel(self, currentPage, totalPages):
        self.footerFrame.setPageLabel(currentPage, totalPages)



    def finish(self):
        self.tileFrameManager.generateResults()
        pass



    def forget(self):
        self.containerFrame.pack_forget()


