from tkinter import *
from threading import Thread

from .home import Home


class InitUi(Thread):
    def __init__(self, messages):
        Thread.__init__(self)
        self.root = Tk()
        self.root.title("All is found")
        self.frame1 = Frame()
        self.frame1.pack(side=LEFT, fill=Y)
        self.frame1.config(bg="skyblue")
        self.home = Home(self.frame1, messages)
        self.refresh_message = self.home.refresh_message

    def run(self):
        self.root.mainloop()
