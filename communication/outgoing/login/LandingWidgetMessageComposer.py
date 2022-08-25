from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class LandingWidgetMessageComposer(MessageComposer):
    def __init__(self):
        super().__init__()
        self.response = Response(outgoing.LandingWidgetMessageComposer)

    def compose(self):
        self.response.write_string("")
        self.response.write_string("")
