from tkinter import *

helv36 = ("Helvetica", 16)


class PopupMessage:
    def __init__(self, top, message):
        self.top = top
        self.message = message['message']
        self.top.geometry("600x250")
        self.top.config(bg="skyblue")
        self.top.title('Message')
        # root frame
        self.root_frame = Frame(self.top)
        self.root_frame.config(bg="skyblue")
        self.root_frame.pack()
        # frame for all info
        self.info_section = Frame(self.root_frame)
        self.info_section.config(bg="skyblue")
        self.info_section.pack()
        # frame for title and detail
        self.left_info_section = Frame(self.info_section)
        self.left_info_section.pack(side=LEFT)
        # frame for contact
        self.right_info_section = Frame(self.info_section)
        self.right_info_section.pack(side=TOP, anchor=NW)
        # title component
        self.title_section = Frame(self.left_info_section)
        self.title_section.pack(side=TOP)
        #self.title_section.config(bg="#3498DB")
        self.title_label = Label(self.title_section, text="Title",font=("Helvetica", 12))#,fg="#FBFCFC")
        self.title_label.pack()
        #self.title_label.config(bg="#3498DB")
        self.title_text = Text(self.title_section, height=1, width=25)
        self.title_text.insert(INSERT, self.message[0])
        self.title_text.configure(font=helv36)
        self.title_text.pack()
        # detail component
        self.detail_section = Frame(self.left_info_section)
        self.detail_section.pack(side=TOP)
        #self.detail_section.config(bg="#3498DB")
        self.detail_label = Label(self.detail_section, text="Detail",font=("Helvetica", 12))#,fg="#FBFCFC")
        #self.detail_label.config(bg="#3498DB")
        self.detail_label.pack()
        self.detail_text = Text(self.detail_section, height=5, width=25)
        self.detail_text.insert(INSERT, self.message[1])
        self.detail_text.configure(font=helv36)
        self.detail_text.pack()
        # contact component
        self.contact_section = Frame(self.right_info_section)
        self.contact_section.pack(side=TOP)
        #self.contact_section.config(bg="#3498DB")
        self.contact_label = Label(self.contact_section, text="Contact",font=("Helvetica", 12))#,fg="#FBFCFC")
        self.contact_label.pack()
       # self.contact_label.config(bg="#3498DB")
        self.contact_text = Text(self.contact_section, height=7, width=25)
        self.contact_text.insert(INSERT, self.message[2])
        self.contact_text.configure(font=helv36)
        self.contact_text.pack()