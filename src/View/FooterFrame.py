import sys
import tkinter as tk
from tkinter import StringVar, ttk

class FooterFrame(ttk.Frame):
    """
    Frame containing page info, and navigation controls

    Attrubute
    ---------
    listManager : ListManager
        controller keeping track of operations run on main list
    pageLayout : PageLayout
        PageLayout is the parent from
    label : StringVar
        text in label used to display page info
    pageControlFrame : tk.Frame
        frame for page controls (next page, and previous page)
    buttonFrame : tk.Frame
        frame for continue and cancel buttons
    contBtn : tk.Button
        continue button
    cancelBtn : tk.Button
        cancel button
    nextBtn : tk.Button
        next page button
    prevBtn : tk.Button
        previous page button
    pageLabel : tk.Label
        label used to display page info


    Methods
    -------
    stringify(curr : int, total : int)
        returns a string with current page info: "current/total"
    setPageLabel(curr : int, total : int)
        sets the string var to update the label
    create()
        draw all widgets
    cont()
        continue on to final step of program
    nextPage()
        display the next page
    prevPage()
        display the previous page

    """

    def __init__(self, container, listManager, pageLayout):
        """
        Parameters
        ----------
        container : ttk.Frame
        listManager : ListManager
        pageLayout : PageLayout
        """

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
        """returns string formatted to display current page over total pages
        
        Parameters
        ----------
        curr : int
            integer representing the current page being viewed
        total : int
            the total number of pages
        """

        return str(curr) + " / " + str(total)



    def setPageLabel(self, curr, total):
        """sets the string var that updates page label content
        
        Parameters
        ----------
        curr : int
            integer representing the current page being viewed
        total : int
            the total number of pages
        """

        newLabel = self.stringify(curr, total)
        self.label.set(newLabel)



    def create(self):
        """draws all of it's widgets"""
        
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
        """continue to next step of program, display the results"""

        self.pageLayout.cont()



    def quit(self):
        """exit the program"""

        sys.exit(0)



    def nextPage(self):
        """show next page"""

        self.pageLayout.nextPage()



    def prevPage(self):
        """show previous page"""

        self.pageLayout.prevPage()

