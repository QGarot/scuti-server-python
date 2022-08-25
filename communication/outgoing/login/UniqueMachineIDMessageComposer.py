from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class UniqueMachineIDMessageComposer(MessageComposer):
    def __init__(self, unique_id):
        super().__init__()
        self.response = Response(outgoing.UniqueMachineIDMessageComposer)
        self.unique_id = unique_id

    def compose(self):
        self.response.write_string(self.unique_id)
