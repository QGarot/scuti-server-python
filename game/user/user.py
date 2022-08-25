from communication.outgoing.message_composer import MessageComposer
from game.user.details import Details
from utils.message_treatment import encode


class User:
    def __init__(self, socket):
        self.socket = socket
        self.details = Details()

    def get_details(self) -> Details:
        """
        Get details
        :return:
        """
        return self.details

    def send(self, message_composer: MessageComposer):
        """
        Send packet to the client
        :param message_composer:
        :return:
        """
        self.socket.send(encode(message_composer))
