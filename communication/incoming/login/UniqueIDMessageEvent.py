"""
Authenticate user class using received SSO ticket
Author: Alex (TheAmazingAussie)
"""
from communication.incoming.message_event import MessageEvent
from game.user.user import User
from network.binary.request import Request


class UniqueIDMessageEvent(MessageEvent):

    @staticmethod
    def handle(user: User, request: Request):
        request.read_string()
        unique_machine_id = request.read_string()
        user.get_details().machine_id = unique_machine_id
