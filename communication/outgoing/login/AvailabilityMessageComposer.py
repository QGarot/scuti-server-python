from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class AvailabilityMessageComposer(MessageComposer):
    def __init__(self):
        super().__init__()
        self.response = Response(outgoing.AvailabilityMessageComposer)

    def compose(self):
        self.response.write_bool(True)
        self.response.write_bool(False)
        self.response.write_bool(True)
