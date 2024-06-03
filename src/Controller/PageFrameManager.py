
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



    # def getPage(self, pageNumb):
    #     return PageFrame(self.model, )



    def updatePageLabel(self, currentPage, totalPages):
        self.footerFrame.setPageLabel(currentPage, totalPages)


    def finish(self):
        self.tileFrameManager.generateResults()
        pass


    def forget(self):
        self.containerFrame.pack_forget()



    # def create(self, pages):
    #     # self.grid(column = 0, row = 0)
    #     self.grid(column = 0, row = 0, sticky = "we", padx = 50)
    #     self.grid_rowconfigure(0, weight = 1)
    #     self.grid_columnconfigure(0, weight = 1)

    #     self.pages = pages
    #     self.pages[0].create()

    # def nextPage(self, current, next):
    #     self.pages[current].pack_forget()
    #     self.pages[next].create()
    #     # self.pages[next].pack()


    # def prevPage(self, current, prev):
    #     self.pages[current].pack_forget()
    #     self.pages[prev].create()
