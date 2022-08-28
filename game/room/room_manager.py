import utils.logger as log
from database.dao.room_dao import RoomDao
from game.room.room import Room


class RoomManager:

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = RoomManager()
            log.info("Room manager loaded!")

        return cls.instance

    def __init__(self):
        self.rooms = {}
        self.models = None

    def load_models(self):
        self.models = RoomDao.get_room_models()

    def get_room_by_id(self, room_id: int) -> Room:
        """
        Return the room with room_id as id
        :param room_id:
        :return:
        """
        if room_id in self.rooms:
            return self.rooms[room_id]
        else:
            room = RoomDao.get_room_by_id(room_id)
            self.add_room(room)
            return room

    def add_room(self, room: Room):
        """
        Add room to rooms dict if it isn't in
        :param room:
        :return: None
        """
        room_id = room.get_data().id
        if room_id not in self.rooms:
            self.rooms[room_id] = room

    def get_player_rooms(self, user_id):
        """
        Return all rooms owned by a user
        :param user_id: the owner id of the rooms
        :return:
        """
        rooms = []

        for room in self.rooms.values():
            if room.get_data().owner_id == user_id:
                rooms.append(room)

        return rooms
