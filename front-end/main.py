from tkinter import *
import threading

from home import Home

groups = [["loss pen at 19th building 4","pink pen mini heart at center","pick me up"]] # title,content, contact
root = Tk()
root.title("All is found")
frame1 = Frame()
frame1.pack(side=LEFT, fill=Y)
Home(frame1,groups)
root.mainloop()
