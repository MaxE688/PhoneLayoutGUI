import tkinter as tk
from tkinter import ttk
from Controller.PageLayout import PageLayout
from View.FooterFrame import FooterFrame
from View.PageFrame import PageFrame

class PageFrameManager:
    def __init__(self, root, model, listManager):
        # super().__init__(parent)
        self.listManager = listManager
        self.containerFrame = ttk.Frame(root)
        self.pageLayout = PageLayout(self.containerFrame, model, self.listManager)
        # self.footerFrame = FooterFrame(self.containerFrame) 

        self.containerFrame.pack()



    # def getPage(self, pageNumb):
    #     return PageFrame(self.model, )






    def create(self, pages):
        # self.grid(column = 0, row = 0)
        self.grid(column = 0, row = 0, sticky = "we", padx = 50)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        self.pages = pages
        self.pages[0].create()

    def nextPage(self, current, next):
        self.pages[current].pack_forget()
        self.pages[next].create()
        # self.pages[next].pack()


    def prevPage(self, current, prev):
        self.pages[current].pack_forget()
        self.pages[prev].create()
