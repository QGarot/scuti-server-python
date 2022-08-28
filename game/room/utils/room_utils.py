from communication.outgoing.room.HeightMapMessageComposer import HeightMapMessageComposer
from communication.outgoing.room.RoomModelMessageComposer import RoomModelMessageComposer
from game.room.room_manager import RoomManager
from game.room.room_model import RoomModel
from game.user.user import User


class RoomUtils:
    @staticmethod
    def load_room(user: User, room_id: int):
        """
        Load room for user session
        :param user:
        :param room_id:
        :return:
        """
        # Room object
        room = RoomManager.get_instance().get_room_by_id(room_id)
        room_model_name = room.get_data().model
        room.model = RoomManager.get_instance().models[room_model_name]

        # Room User
        user.room_user.room = room

        user.send(RoomModelMessageComposer(room_model_name, room_id))

    @staticmethod
    def load_heightmap(user: User, room_model: RoomModel):
        """
        Load heightmap, walls, items.
        :param user:
        :param room_model:
        :return:
        """
        user.send(HeightMapMessageComposer(room_model))
