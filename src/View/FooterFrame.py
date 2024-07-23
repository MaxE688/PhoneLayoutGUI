import sys
import tkinter as tk
from tkinter import StringVar, ttk

class FooterFrame(ttk.Frame):
    def __init__(self, container, listManager, pageLayout):

        s = ttk.Style()
        s.configure('Foot.TFrame')

        super().__init__(container, style = 'Foot.TFrame')

        self.listManager = listManager
        self.pageLayout = pageLayout
        
        l = self.stringify(self.pageLayout.currentPage + 1, self.listManager.getPageCount()) 
        self.label = StringVar()
        self.label.set(l)

        self.pageControlFrame = tk.Frame(self)
        self.buttonFrame = tk.Frame(self)

        self.contBtn = tk.Button(self.buttonFrame, text = "Continue", command = self.cont)
        self.cancelBtn = tk.Button(self.buttonFrame, text = "Cancel", command = self.quit)
        self.nextBtn = tk.Button(self.pageControlFrame, text = ">", command = self.nextPage)
        self.prevBtn = tk.Button(self.pageControlFrame, text = "<", command = self.prevPage)
        self.pageLabel = tk.Label(self.pageControlFrame, textvariable = self.label)
        self.create()



    def stringify(self, curr, total):
        return str(curr) + " / " + str(total)



    def setPageLabel(self, curr, total):
        newLabel = self.stringify(curr, total)
        self.label.set(newLabel)



    def create(self):
        
        self.pack()
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        self.contBtn.grid(column = 2, row = 1, columnspan = 3, pady = (10))
        self.cancelBtn.grid(column = 5, row = 1, columnspan = 3)

        self.nextBtn.grid(column = 6, row = 0, columnspan = 2)
        self.pageLabel.grid(column = 4, row = 0, columnspan = 2)
        self.prevBtn.grid(column = 2, row = 0, columnspan = 2, padx = (0, 0))

        self.nextBtn.grid_rowconfigure(0, weight = 1)
        self.nextBtn.grid_columnconfigure(0, weight = 1)

        self.pageLabel.grid_rowconfigure(0, weight = 1)
        self.pageLabel.grid_columnconfigure(0, weight = 1)

        self.prevBtn.grid_rowconfigure(0, weight = 1)
        self.prevBtn.grid_columnconfigure(0, weight = 1)

        self.contBtn.grid_rowconfigure(0, weight = 2)
        self.contBtn.grid_columnconfigure(0, weight = 1)

        self.cancelBtn.grid_rowconfigure(0, weight = 2)
        self.cancelBtn.grid_columnconfigure(0, weight = 1)

        self.pageControlFrame.pack()
        self.buttonFrame.pack()



    def cont(self):
        self.pageLayout.cont()



    def quit(self):
        sys.exit(0)



    def nextPage(self):
        self.pageLayout.nextPage()



    def prevPage(self):
        self.pageLayout.prevPage()

