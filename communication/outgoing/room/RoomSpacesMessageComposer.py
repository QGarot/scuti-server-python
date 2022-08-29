from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class RoomSpacesMessageComposer(MessageComposer):
    def __init__(self, space: str, data: str):
        super().__init__()
        self.response = Response(outgoing.RoomSpacesMessageComposer)
        self.space = space
        self.data = data

    def compose(self):
        self.response.write_string(self.space)
        self.response.write_string(self.data)
