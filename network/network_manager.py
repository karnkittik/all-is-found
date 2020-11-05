from scapy.all import *
import pickle

from threading import Thread


class NetworkManger(Thread):
    def __init__(self, messages, refresh_messages):
        Thread.__init__(self)
        self.messages = messages
        self.refresh_messages = refresh_messages
        self.set_message = set()
        pass

    def receive_message(self):
        print("Waiting for receiving...")
        pkt = sniff(filter='icmp', prn=self.print_pkt)

    def print_pkt(self, pkt):
        try:
            a = pkt[Raw].load
            decode = pickle.loads(a)
            if (decode['id'] not in self.messages.get_message_ids()):
                self.messages.add_message(decode)
                self.messages.add_message_id(decode['id'])
                self.refresh_messages()
        except Exception as e:
            print(e)
            pass

    def run(self):
        self.receive_message()
