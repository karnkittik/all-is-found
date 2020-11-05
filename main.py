from front_end.main import InitUi
from network.network_manager import NetworkManger


class Messages:
    def __init__(self):
        self.messages = [{
            'id':
            '52255155546d446fd45dv',
            'ttl':
            1,
            'message': [
                "loss pen at 19th building 4", "pink pen mini heart at center",
                "pick me up"
            ]
        }]
        self.message_ids = set()

    def get_messages(self):
        return self.messages

    def add_message(self, message):
        self.messages.append(message)

    def get_message_ids(self):
        return self.message_ids

    def add_message_id(self, messageId):
        self.message_ids.add(messageId)


if __name__ == "__main__":
    messages = Messages()
    ui = InitUi(messages)

    network_thread = NetworkManger(messages, ui.refresh_message)
    network_thread.daemon = True
    network_thread.start()

    # ui.home.set_network(network_thread)

    ui.run()