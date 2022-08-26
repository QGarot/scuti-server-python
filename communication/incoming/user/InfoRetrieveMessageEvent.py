from communication.incoming.message_event import MessageEvent
from communication.outgoing.user.UserObjectMessageComposer import UserObjectMessageComposer
from game.user.user import User
from network.binary.request import Request


class InfoRetrieveMessageEvent(MessageEvent):

    @staticmethod
    def handle(user: User, request: Request):
        user.send(UserObjectMessageComposer(user.get_details()))
