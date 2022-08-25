from communication.incoming.message_event import MessageEvent
from game.user.user import User
from game.user.user_manager import UserManager
from network.binary.request import Request


class AuthenticateMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: Request):
        sso_ticket = request.read_string()
        UserManager.get_instance().authenticate_user(user, sso_ticket)

