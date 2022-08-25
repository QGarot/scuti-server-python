import utils.logger
import communication.incoming.header as headers
from communication.incoming.login.authenticate_message_event import AuthenticateMessageEvent
from game.user.user import User
from network.binary.request import Request


class MessageHandler:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = MessageHandler()

        return cls.instance

    def __init__(self):
        self.incoming = {
            headers.AuthenticateMessageEvent: AuthenticateMessageEvent()
        }

    def handle(self, user: User, header: int, request: Request):
        if header in self.incoming:
            utils.logger.log_packet(header, "OK")
            self.incoming[header].handle(user, request)
        else:
            utils.logger.log_packet(header, "Packet not saved")
