from communication.incoming.message_event import MessageEvent
from communication.outgoing.user.AvatarAspectUpdateMessageComposer import AvatarAspectUpdateMessageComposer
from communication.outgoing.user.UserObjectMessageComposer import UserObjectMessageComposer
from game.user.user import User
from game.user.user_manager import UserManager
from network.binary.request import Request


class ChangeAppearanceMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: Request):
        gender = request.read_string()
        figure = request.read_string()

        # Edit details
        user.get_details().figure = figure
        user.get_details().gender = gender

        # Save in database
        UserManager.save(user.get_details())

        user.send(AvatarAspectUpdateMessageComposer(figure, gender))
        user.send(UserObjectMessageComposer(user.get_details()))
