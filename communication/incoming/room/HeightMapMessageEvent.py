from communication.incoming.message_event import MessageEvent
from game.room.utils.room_utils import RoomUtils
from game.user.user import User
from network.binary.request import Request


class HeightMapMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: Request):
        room = user.room_user.room
        RoomUtils.load_heightmap(user, room)
