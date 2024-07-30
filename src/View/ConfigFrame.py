import tkinter as tk
from tkinter import ttk

class ConfigFrame(ttk.Frame):
    """
    Frame for setting initial config string

    Attributes
    ----------
    fm : FrameManager
        instace of main controller
    title : str
        title of the window
    text : tk.Text
        text widget


    Methods
    -------
    newConfig()
        Event listener for New Config button
    submit()
        Event listener for Submit button
    cancel()
        Event listner for Cancel button


    """
    
    def __init__(self, fm):
        """
        Parameters
        ----------
        fm : FrameManager
        """

        super().__init__(fm.root, padding=(30, 15, 30, 15))

        self.fm = fm

        self.title = "Change Phone Layout: Set Configuration - " + str(fm.model)

        label1 = tk.Label(self, text = "Enter button configuration here:")
        self.text = tk.Text(self)

        newConfigBtn = tk.Button(self, text = "New Config")
        newConfigBtn['command'] = self.newConfig

        submitBtn = tk.Button(self, text = "Submit")
        submitBtn['command'] = self.submit

        backBtn = tk.Button(self, text = "Back")
        backBtn['command'] = self.cancel

        self.pack()
        label1.grid(column  = 1, row = 1, columnspan = 5)
        self.text.grid(column = 1, row = 2, columnspan = 5)
        newConfigBtn.grid(column = 2, row = 4, sticky = "e", padx=(450, 50))
        submitBtn.grid(column = 4, row = 4, sticky = "e")
        backBtn.grid(column = 5, row = 4, sticky = "e", padx = (0, 10))

        tk.Frame(self, height = 10).grid(column = 0, row = 3)


    def newConfig(self):
        """Event listener for New Config button"""

        print("config Frame new config")
        self.fm.initPhoneFrame(self, "")



    def submit(self):
        """Event listener for Submit button"""
        
        cfg = self.text.get("1.0", "end-1c")
        if cfg == "":
            print("MessageBox(\"Cannot submit blank config.\")")
        else:
            self.fm.initPhoneFrame(self, cfg)



    def cancel(self):
        """Event listener for Cancel button"""
        
        print('Config Frame cancel')
        self.fm.selectModelFrame(self)
