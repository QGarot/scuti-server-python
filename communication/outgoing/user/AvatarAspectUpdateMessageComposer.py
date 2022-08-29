from communication.outgoing.message_composer import MessageComposer
import communication.outgoing.header as outgoing
from network.binary.response import Response


class AvatarAspectUpdateMessageComposer(MessageComposer):
    def __init__(self, figure: str, gender: str):
        super().__init__()
        self.response = Response(outgoing.AvatarAspectUpdateMessageComposer)
        self.figure = figure
        self.gender = gender

    def compose(self):
        self.response.write_string(self.figure)
        self.response.write_string(self.gender)

