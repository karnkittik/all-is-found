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

    # def send_message(self, message):
    #     print("NETWORK SENT: ", end="")
    #     message["id"] = str(Ether().src) + str(int(time.time() // 1))
    #     self.set_message.add(message['id'])
    #     print(message)
    #     a = IP()
    #     a.dst = '169.254.255.255'  #169.254.150.255
    #     a.ttl = 5
    #     del (a.getlayer(IP).chksum)
    #     b = ICMP()
    #     p = a / b
    #     mess = pickle.dumps(message)
    #     sendp(Ether() / p / mess)

    def receive_message(self):
        print("Waiting for receiving...")
        pkt = sniff(filter='icmp', prn=self.print_pkt)

    def print_pkt(self, pkt):
        try:
            a = pkt[Raw].load  #binary
            print(a)
            decode = pickle.loads(a)
            print(decode)
            if (decode['id'] not in self.messages.get_message_ids()):
                print("ee")
                self.messages.add_message(decode)
                print("ff")
                self.messages.add_message_id(decode['id'])
                print("pp")
                self.refresh_messages()
                print("bb")
        except Exception as e:
            print(e)
            pass

    def run(self):
        self.receive_message()
