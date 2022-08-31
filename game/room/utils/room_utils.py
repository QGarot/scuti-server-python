from communication.outgoing.room.FloorMapMessageComposer import FloorMapMessageComposer
from communication.outgoing.room.HeightMapMessageComposer import HeightMapMessageComposer
from communication.outgoing.room.RoomModelMessageComposer import RoomModelMessageComposer
from communication.outgoing.room.RoomSpacesMessageComposer import RoomSpacesMessageComposer
from communication.outgoing.room.UserDisplayMessageComposer import UserDisplayMessageComposer
from communication.outgoing.room.UserStatusMessageComposer import UserStatusMessageComposer
from game.room.room import Room
from game.room.room_manager import RoomManager
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
        # Create room object
        room = RoomManager.get_instance().get_room_by_id(room_id)
        room_model_name = room.get_data().model
        room.model = RoomManager.get_instance().models[room_model_name]

        # Set room user properties
        user.room_user.room = room
        user.room_user.x = room.get_model().door_x
        user.room_user.y = room.get_model().door_y
        user.room_user.z = room.get_model().door_z
        user.room_user.rotation = room.get_model().door_rotation
        user.room_user.head_rotation = room.get_model().door_rotation
        user.room_user.virtual_id = room.get_virtual_counter()

        user.send(RoomModelMessageComposer(room_model_name, room_id))

        floor_data = int(room.get_data().floor)
        wall_data = int(room.get_data().wall)

        # Floor design
        if floor_data > 0:
            user.send(RoomSpacesMessageComposer("floor", room.get_data().floor))

        # Wall design
        if wall_data > 0:
            user.send(RoomSpacesMessageComposer("wall", room.get_data().wall))

        # Landscape design
        user.send(RoomSpacesMessageComposer("landscape", room.get_data().landscape))
        # session.send(PrepareRoomMessageComposer(self.data.id))

    @staticmethod
    def load_heightmap(user: User, room: Room):
        """
        Load heightmap, walls, items etc...
        :param room:
        :param user:
        :return:
        """
        user.send(HeightMapMessageComposer(room.get_model()))
        user.send(FloorMapMessageComposer(room))

        # Display self
        user.send(UserDisplayMessageComposer([user]))
        user.send(UserStatusMessageComposer([user]))

        # Display users for client
        #session.send(UserDisplayMessageComposer(self.entities))
        #session.send(UserStatusMessageComposer(self.entities))
