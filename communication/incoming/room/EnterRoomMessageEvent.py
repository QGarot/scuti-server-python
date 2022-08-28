from communication.incoming.message_event import MessageEvent
from game.room.utils.room_utils import RoomUtils
from game.user.user import User
from network.binary.request import Request


class EnterRoomMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: Request):
        room_id = request.read_int()
        RoomUtils.load_room(user, room_id)
