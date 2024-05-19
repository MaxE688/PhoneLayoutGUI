import sys
import tkinter as tk

from tkinter import ttk

class FooterFrame(ttk.Frame):
    def __init__(self, controller):

        s = ttk.Style()
        s.configure('Foot.TFrame')

        super().__init__(controller, style = 'Foot.TFrame')




        self.tileFM = controller
        label = str(self.tileFM.currentPage + 1) + " / " + str(self.tileFM.pageCount)
        # label = str(self.tileFM.currentPage) + " / " + str(self.tileFM.pageCount)

        self.pageControlFrame = tk.Frame(self)
        self.buttonFrame = tk.Frame(self)

        self.contBtn = tk.Button(self.buttonFrame, text = "Continue", command = self.cont)
        self.cancelBtn = tk.Button(self.buttonFrame, text = "Cancel", command = self.quit)
        self.nextBtn = tk.Button(self.pageControlFrame, text = ">", command = self.nextPage)
        self.prevBtn = tk.Button(self.pageControlFrame, text = "<", command = self.prevPage)
        self.pageLabel = tk.Label(self.pageControlFrame, text = label)





    def create(self):
        self.grid(column = 0, row = 1, sticky = "we")
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        # tk.Frame(self, width = 25, height = 25, bg = 'green').grid(column = 0, row = 0)
        # tk.Frame(self, width = 25, height = 25, bg = 'yellow').grid(column = 1, row = 0)
        self.pageControlFrame.pack()
        self.buttonFrame.pack()

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


    def cont(self):
        print("continue")
        self.tileFM.cont()

    def quit(self):
        sys.exit(0)

    def nextPage(self):
        print("next page")
        self.tileFM.nextPage()


    def prevPage(self):
        print("prev page")

        self.tileFM.prevPage()

    def updateFrame(self):
        self.pageControlFrame.pack_forget()
        self.buttonFrame.pack_forget()

    def updateLabel(self, curr):
        label = str(curr + 1) + " / " + str(self.tileFM.pageCount)
        self.pageLabel.destroy()
        # self.prevBtn.grid_forget()
        self.pageLabel = tk.Label(self.pageControlFrame, text = label)
        self.pageLabel.grid(column = 4, row = 0, columnspan = 2)
        # self.prevBtn.pack()
