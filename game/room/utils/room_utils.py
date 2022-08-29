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

        floor_data = int(room.get_data().floor)
        wall_data = int(room.get_data().wall)

        # Floor design
        # if floor_data > 0:
        #     session.send(RoomSpacesMessageComposer("floor", self.data.floor))

        # Wall design
        # if wall_data > 0:
        #     session.send(RoomSpacesMessageComposer("wall", self.data.wall))

        # Landscape design
        # session.send(RoomSpacesMessageComposer("landscape", self.data.landscape))
        # session.send(PrepareRoomMessageComposer(self.data.id))

    @staticmethod
    def load_heightmap(user: User, room_model: RoomModel):
        """
        Load heightmap, walls, items.
        :param user:
        :param room_model:
        :return:
        """
        user.send(HeightMapMessageComposer(room_model))
        #session.send(FloorMapMessageComposer(self))

        # Display self
        #self.send(UserDisplayMessageComposer([session]))
        #self.send(UserStatusMessageComposer([session]))

        # Display users for client
        #session.send(UserDisplayMessageComposer(self.entities))
        #session.send(UserStatusMessageComposer(self.entities))
