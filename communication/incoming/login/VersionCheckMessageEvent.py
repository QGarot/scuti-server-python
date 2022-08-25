"""
Check release of SWF version
Author: Alex (TheAmazingAussie)
"""

from communication.incoming.message_event import MessageEvent
from game.user.user import User
from network.binary.request import Request


class VersionCheckMessageEvent(MessageEvent):

    @staticmethod
    def handle(user: User, request: Request):
        swf_revision = request.read_string()
        print("Version check, swf revision: " + swf_revision)
