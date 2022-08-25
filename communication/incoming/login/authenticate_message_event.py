from communication.incoming.message_event import MessageEvent
from network.binary.request import Request


class AuthenticateMessageEvent(MessageEvent):
    @staticmethod
    def handle(connection, request: Request):
        sso_ticket = request.read_string()
        print(sso_ticket)
