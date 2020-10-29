from scapy.all import *
import pickle
class NetworkManger:
    def __init__(self, add_message):
        self.add_message = add_message
        self.receive_message()
        pass

    def send_message(self, message):
        print("NETWORK SENT: ", end="")
        print(message)     
        a = IP()
        a.dst = '169.254.255.255' #169.254.150.255
        b = ICMP()
        p = a/b
        mess = pickle.dumps(message)
        sendp(Ether()/p/mess)

    def receive_message(self):
        pkt = sniff(filter='icmp',prn=print_pkt)
    def print_pkt(pkt):
        try:
            a = pkt[Raw] #binary
            decode = pickle.loads(a)
            self.add_message(message)
        except:
            pass
        
