from typing import Optional

from database.database import Database
from game.room.room import Room
from game.room.room_model import RoomModel


class RoomDao:

    @staticmethod
    def get_room_by_id(room_id: int) -> Optional[Room]:
        select = Database.get_instance().select(attributes="*", table_name="rooms",
                                                sql_condition="id = " + str(room_id))
        room = None
        if len(select) == 1:
            room = Room()
            room.fill(select[0])

        return room

    @staticmethod
    def get_room_models() -> dict:
        models = dict()
        select = Database.get_instance().select(attributes="*", table_name="room_models")
        for row in select:
            model_name = row[0]
            door_x = row[1]
            door_y = row[2]
            door_z = row[3]
            door_rot = row[4]
            heightmap = row[5]
            models[row[0]] = RoomModel(model_name, heightmap, door_x, door_y, door_z, door_rot)

        return models

    @staticmethod
    def fill_data(room: Room, row: tuple) -> None:
        """
         Fill instance with given row data
         :param room: the data instance to fill
         :param row: the row fected with MySQL
         :return:
         """
        room.get_data().id = row[0]
        room.get_data().name = row[1]
        room.get_data().type = row[2]
        room.get_data().owner_id = row[4]
        room.get_data().group_id = row[5]
        room.get_data().description = row[7]
        room.get_data().password = row[8]
        room.get_data().users_now = row[9]
        room.get_data().users_max = row[10]
        room.get_data().model = row[11]
        room.get_data().wall = row[12]
        room.get_data().floor = row[13]
        room.get_data().landscape = row[14]
        room.get_data().tags = row[15].split(",")
        room.get_data().trade_state = row[16]

        _state = row[17]

        if _state == "OPEN":
            room.get_data().state == 0

        if _state == "INVISIBLE":
            room.get_data().state == 3

        if _state == "DOORBELL":
            room.get_data().state == 1

        if _state == "PASSWORD":
            room.get_data().state == 2

        room.get_data().score = row[18]
        room.get_data().category = row[19]
        room.get_data().allow_pets = row[20] == 1
        room.get_data().allow_pets_eat = row[21] == 1
        room.get_data().allow_walk_through = row[22] == 1
