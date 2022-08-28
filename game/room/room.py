from communication.outgoing.message_composer import MessageComposer
from game.room.room_data import RoomData
from game.room.room_model import RoomModel
from game.user.user import User


class Room:
    def __init__(self):
        self.room_data = RoomData()
        self.model = None
        self.mapping = None
        self.entities = []

    def get_users(self) -> list:
        """
        Return list of users in this room
        :return:
        """
        users = []
        for entity in self.entities:
            if type(entity) == User:
                users.append(entity)

        return users

    def send(self, message_composer: MessageComposer):
        """
        Send message to all users in this room
        :param message_composer:
        :return:
        """
        for user in self.get_users():
            user.send(message_composer)

    def get_data(self) -> RoomData:
        return self.room_data

    def get_model(self) -> RoomModel:
        return self.model

    def fill(self, row: tuple):
        """
        Fill instance with given row data
        :param row: the row fected with MySQL
        :return:
        """
        self.get_data().id = row[0]
        self.get_data().name = row[1]
        self.get_data().type = row[2]
        self.get_data().owner_id = row[4]
        self.get_data().group_id = row[5]
        self.get_data().description = row[7]
        self.get_data().password = row[8]
        self.get_data().users_now = row[9]
        self.get_data().users_max = row[10]
        self.get_data().model = row[11]
        self.get_data().wall = row[12]
        self.get_data().floor = row[13]
        self.get_data().landscape = row[14]
        self.get_data().tags = row[15].split(",")
        self.get_data().trade_state = row[16]

        _state = row[17]

        if _state == "OPEN":
            self.get_data().state == 0

        if _state == "INVISIBLE":
            self.get_data().state == 3

        if _state == "DOORBELL":
            self.get_data().state == 1

        if _state == "PASSWORD":
            self.get_data().state == 2

        self.get_data().score = row[18]
        self.get_data().category = row[19]
        self.get_data().allow_pets = row[20] == 1
        self.get_data().allow_pets_eat = row[21] == 1
        self.get_data().allow_walk_through = row[22] == 1
