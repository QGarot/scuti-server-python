from game.user.user import User
from network.binary.request import Request


class MessageEvent:
    @staticmethod
    def handle(user: User, request: Request):
        pass
