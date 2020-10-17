from front_end.popup_message import PopupMessage
from tkinter import *

from .new_message import NewMessage
from .popup_message import PopupMessage

from network.network_manager import NetworkManger

class Home:
    def __init__(self, root_frame, messages):
        self.network_manager = NetworkManger()
        self.root_frame = root_frame
        self.messages = messages

        self.home_head = Frame(root_frame)
        self.home_head.config(bg="skyblue")
        self.home_head.pack()

        self.header = Label(self.home_head, text="Message Panel", bg="skyblue", font=("Helvetica", 14))
        self.header.grid(row=0, column=0,padx=110, pady=5)

        self.new_message_btn = Button(self.home_head,
                                      text='New Message',
                                      font=("Helvetica", 12),
                                      bg= "#FFBA31",
                                      command=self.open_new_message)
        self.new_message_btn.grid(row=0, column=1)

        self.home_body = Frame(root_frame)
        self.home_body.pack()

        self.list_message = Listbox(self.home_body, width=50, font=("Helvetica", 12))
        self.list_message.bind('<<ListboxSelect>>', lambda event: self.show_message()) 
        self.list_message.pack(side=LEFT)
        self.scrollbar = Scrollbar(self.home_body, orient="vertical")
        self.scrollbar.config(command=self.list_message.yview)
        self.scrollbar.pack(side=LEFT, fill=Y)
        self.list_message.config(yscrollcommand=self.scrollbar.set)
        self.refresh_message()
    #onclick
    def show_message(self):
        # curselection() returns a tuple of indexes selected in listbox
        selection = self.list_message.curselection()
        if len(selection) > 0:
            index = selection[0]
            top = Toplevel()
            PopupMessage(top, self.messages[index])
            # print("Clicked indexes: {0}".format(selection))
    #for moc
    def send_message(self, message):
        self.network_manager.send_message(message)

    def add_message(self, message):
        self.messages.append(message)
        self.send_message(message)

    def open_new_message(self):
        top = Toplevel()
        NewMessage(top, self.add_message)
        self.home_body.wait_window(top)

        self.refresh_message()
        # print(self.all_group.get_alL_group_name())

    def refresh_message(self):
        #self.group_id = []
        self.list_message.delete(0, 'end')
        for (title, content, contact) in self.messages:
            self.list_message.insert(END, "Title: " + title)
        # self.all_group.is_change_to_view = False
        self.home_body.update()
