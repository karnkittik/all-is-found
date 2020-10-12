from tkinter import *
import threading

from .home import Home


class InitUi:
    def __init__(self):
        self.groups = [[
            "loss pen at 19th building 4", "pink pen mini heart at center",
            "pick me up"
        ]]  # title,content, contact
        self.root = Tk()
        self.root.title("All is found")
        self.frame1 = Frame()
        self.frame1.pack(side=LEFT, fill=Y)
        Home(self.frame1, self.groups)

    def start(self):
        self.root.mainloop()
