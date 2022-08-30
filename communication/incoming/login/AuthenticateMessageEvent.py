from communication.incoming.message_event import MessageEvent
from communication.outgoing.login.AuthenticationOKMessageComposer import AuthenticationOKMessageComposer
from communication.outgoing.login.AvailabilityMessageComposer import AvailabilityMessageComposer
from communication.outgoing.login.HomeRoomMessageComposer import HomeRoomMessageComposer
from communication.outgoing.login.LandingWidgetMessageComposer import LandingWidgetMessageComposer
from communication.outgoing.login.UniqueMachineIDMessageComposer import UniqueMachineIDMessageComposer
from game.user.user import User
from game.user.user_manager import UserManager
from network.binary.request import Request


class AuthenticateMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: Request):
        sso_ticket = request.read_string()
        UserManager.get_instance().authenticate_user(user, sso_ticket)

        user.send(AuthenticationOKMessageComposer())
        user.send(UniqueMachineIDMessageComposer(user.get_details().machine_id))
        user.send(HomeRoomMessageComposer(4, True))
        user.send(LandingWidgetMessageComposer())
        user.send(AvailabilityMessageComposer())

        user.send_motd_notification("Hi " + user.get_details().username + ", Welcome to Scuti :)")
