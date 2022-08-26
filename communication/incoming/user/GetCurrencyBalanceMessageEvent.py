from communication.incoming.message_event import MessageEvent
from communication.outgoing.user.CreditsBalanceMessageComposer import CreditsBalanceMessageComposer
from game.user.user import User
from network.binary.request import Request


class CurrencyBalanceMessageEvent(MessageEvent):

    @staticmethod
    def handle(user: User, request: Request):
        user.send(CreditsBalanceMessageComposer(user.get_details().credits))
