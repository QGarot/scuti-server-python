from communication.outgoing.message_composer import MessageComposer
from game.user.details import Details
from network.binary.response import Response
import communication.outgoing.header as outgoing


class UserObjectMessageComposer(MessageComposer):
    def __init__(self, details: Details):
        super().__init__()
        self.response = Response(outgoing.UserObjectMessageComposer)
        self.details = details

    def compose(self):
        self.response.write_int(self.details.id)
        self.response.write_string(self.details.username)
        self.response.write_string(self.details.figure)
        self.response.write_string("M")
        self.response.write_string(self.details.motto)
        self.response.write_string("")
        self.response.write_bool(False) # ?
        self.response.write_int(0)  # Respect
        self.response.write_int(3)  # Daily Respect Points
        self.response.write_int(3)  # Daily Pet Respect Points
        self.response.write_bool(True)
        self.response.write_string("1448526834")
        self.response.write_bool(True)
        self.response.write_bool(False)
