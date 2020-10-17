from tkinter import *

helv36 = ("Helvetica", 16)


class NewMessage:
    def __init__(self, top, add_message):
        self.add_message = add_message
        self.top = top
        self.top.geometry("600x250")
        self.top.config(bg="skyblue")
        self.top.title('New message')

        # root frame
        self.root_frame = Frame(self.top)
        self.root_frame.config(bg="skyblue")
        self.root_frame.pack()
        # frame for all inputs
        self.input_section = Frame(self.root_frame)
        self.input_section.config(bg="skyblue")
        self.input_section.pack()
        # frame for title and detail
        self.left_input_section = Frame(self.input_section)
        self.left_input_section.pack(side=LEFT)
        # frame for contact
        self.right_input_section = Frame(self.input_section)
        self.right_input_section.pack(side=TOP, anchor=NW)
        # title component
        self.title_section = Frame(self.left_input_section)
        self.title_section.pack(side=TOP)
        self.title_label = Label(self.title_section, text="Title",font=("Helvetica", 12))
        self.title_label.pack()
        self.title_text = Text(self.title_section, height=1, width=25)
        self.title_text.configure(font=helv36)
        self.title_text.pack()
        # detail component
        self.detail_section = Frame(self.left_input_section)
        self.detail_section.pack(side=TOP)
        self.detail_label = Label(self.detail_section, text="Detail",font=("Helvetica", 12))
        self.detail_label.pack()
        self.detail_text = Text(self.detail_section, height=5, width=25)
        self.detail_text.configure(font=helv36)
        self.detail_text.pack()
        # contact component
        self.contact_section = Frame(self.right_input_section)
        self.contact_section.pack(side=TOP)
        self.contact_label = Label(self.contact_section, text="Contact",font=("Helvetica", 12))
        self.contact_label.pack()
        self.contact_text = Text(self.contact_section, height=7, width=25)
        self.contact_text.configure(font=helv36)
        self.contact_text.pack()

        self.submit_btn = Button(self.root_frame,
                                 text="Submit",
                                 padx=15,pady=3,
                                 font=("Helvetica", 12),
                                 bg= "#FFBA31",
                                 command=self.on_submit)
        self.submit_btn.pack(pady=10)

    def on_submit(self):
        message = []
        message.append(self.title_text.get("1.0", 'end-1c'))
        message.append(self.detail_text.get("1.0", 'end-1c'))
        message.append(self.contact_text.get("1.0", 'end-1c'))
        self.add_message(message)
        self.top.destroy()
