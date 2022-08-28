import utils.logger
import communication.incoming.header as headers
from communication.incoming.login.UniqueIDMessageEvent import UniqueIDMessageEvent
from communication.incoming.login.VersionCheckMessageEvent import VersionCheckMessageEvent
from communication.incoming.login.AuthenticateMessageEvent import AuthenticateMessageEvent
from communication.incoming.room.EnterRoomMessageEvent import EnterRoomMessageEvent
from communication.incoming.room.HeightMapMessageEvent import HeightMapMessageEvent
from communication.incoming.user.GetCurrencyBalanceMessageEvent import CurrencyBalanceMessageEvent
from communication.incoming.user.InfoRetrieveMessageEvent import InfoRetrieveMessageEvent
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
        """
        Here register all incoming headers
        """
        self.incoming = {
            headers.AuthenticateMessageEvent: AuthenticateMessageEvent(),
            headers.UniqueIDMessageEvent: UniqueIDMessageEvent(),
            headers.VersionCheckMessageEvent: VersionCheckMessageEvent(),

            headers.InfoRetrieveMessageEvent: InfoRetrieveMessageEvent(),
            headers.GetCurrencyBalanceMessageEvent: CurrencyBalanceMessageEvent(),

            headers.EnterRoomMessageEvent: EnterRoomMessageEvent(),
            headers.HeightMapMessageEvent: HeightMapMessageEvent(),
        }

    def handle(self, user: User, header: int, request: Request):
        """
        Handle a user message (incoming)
        :param user:
        :param header:
        :param request:
        :return:
        """
        if header in self.incoming:
            utils.logger.log_packet(header, "OK")
            self.incoming[header].handle(user, request)
        else:
            utils.logger.log_packet(header, "Packet not saved")
