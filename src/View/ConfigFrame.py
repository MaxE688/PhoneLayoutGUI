import tkinter as tk
from tkinter import ttk

class ConfigFrame(ttk.Frame):
    def __init__(self, fm):
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

        # Border spacing
        # tk.Frame(self, width = 40, height = 15).grid(column = 0, row = 5)
        # tk.Frame(self, width = 40).grid(column = 6, row = 4)

        # Button spacing
        # tk.Frame(self, width = 450).grid(column = 1, row = 4)
        # tk.Frame(self, width = 25).grid(column = 3, row = 4)
        tk.Frame(self, height = 10).grid(column = 0, row = 3)
        # fm.root.center()


    def newConfig(self):
        print("config Frame new config")

    def submit(self):

        cfg = self.text.get("1.0", "end-1c")
        if cfg == "":
            print("MessageBox(\"Cannot submit blank config.\")")
        else:
            self.fm.mainFrame(cfg)

    def cancel(self):
        print('Config Frame cancel')
        self.fm.selectModelFrame(self)
