import tkinter as tk
from tkinter import ttk

class ParentModelFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


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
