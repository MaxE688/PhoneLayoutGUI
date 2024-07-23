import tkinter as tk
from tkinter import ttk


class ResultsFrame(ttk.Frame):
    
    def __init__(self, parent, resultString):

        super().__init__(parent)
        self.pack()

        label = tk.Label(self, text = "Copy the button configuration below: ")
        textWidget = tk.Text(self)

        for i, string in enumerate(resultString):
            print()
            print(string)
            print()
            print(str(type(i)) + ": " + str(i))
            string += "\n"
            textWidget.insert(str(i*6) + ".0", string)

        label.pack()
        textWidget.pack()
