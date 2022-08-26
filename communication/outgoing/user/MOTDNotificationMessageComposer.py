from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class MOTDNotificationMessageComposer(MessageComposer):
    def __init__(self, msg: str):
        super().__init__()
        self.response = Response(outgoing.MOTDMessageComposer)
        self.msg = msg

    def compose(self):
        self.response.write_int(1)
        self.response.write_string(self.msg)
