from communication.outgoing.message_composer import MessageComposer
from communication.outgoing.user.MOTDNotificationMessageComposer import MOTDNotificationMessageComposer
from game.room.room_user import RoomUser
from game.user.details import Details
from utils.message_treatment import encode


class User:
    def __init__(self, socket):
        self.socket = socket
        self.details = Details()
        self.room_user = RoomUser()

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

    def send_motd_notification(self, msg: str):
        """
        Send alert to this user
        :param msg:
        :return:
        """
        self.send(MOTDNotificationMessageComposer(msg))

    def fill_data(self, row: tuple):
        """
        Fill user details thanks to row, get with SQL query
        """
        self.get_details().id = row[0]
        self.get_details().username = row[1]
        self.get_details().motto = row[3]
        self.get_details().figure = row[4]
        self.get_details().rank = row[2]
        self.get_details().credits = row[5]
        self.get_details().gender = row[6]
