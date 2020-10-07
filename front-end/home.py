from tkinter import *


class Home:
    def __init__(self,root_frame,messages):
        self.messages = messages
        
        self.home_head = Frame(root_frame)
        self.home_head.pack()

        self.header = Label(self.home_head, text="Message Panel",font="10")
        self.header.grid(row=0, column=0)

        self.new_message_btn = Button(
            self.home_head, text='New Message',font="10", command=self.new_message)
        self.new_message_btn.grid(row=0, column=1)


        self.home_body = Frame(root_frame)
        self.home_body.pack()

        self.list_message = Listbox(self.home_body, width =50,font="8")
        self.list_message.pack(side=LEFT)

        self.scrollbar = Scrollbar(self.home_body, orient="vertical")
        self.scrollbar.config(command=self.list_message.yview)
        self.scrollbar.pack(side=LEFT, fill=Y)
        self.list_message.config(yscrollcommand=self.scrollbar.set)
        self.refresh_message()

    #for moc
    def new_message(self):
        msg = ["Hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","content","contact"]
        self.messages.append(msg)
        for ( title,content, contact) in [msg]:
            self.list_message.insert(END,
                 "Title:"+title )#command = self.read_content(title,content,contact))
        self.home_body.update()
        # print(self.all_group.get_alL_group_name())

        
    def refresh_message(self):
        #self.group_id = []
        for ( title,content, contact) in self.messages:
            self.list_message.insert(END,
                 "Title:"+title )
        # self.all_group.is_change_to_view = False
        self.home_body.update()

    







