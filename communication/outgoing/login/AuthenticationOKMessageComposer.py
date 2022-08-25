from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class AuthenticationOKMessageComposer(MessageComposer):
    def __init__(self):
        super().__init__()
        self.response = Response(outgoing.AuthenticationOKMessageComposer)
