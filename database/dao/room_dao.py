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
