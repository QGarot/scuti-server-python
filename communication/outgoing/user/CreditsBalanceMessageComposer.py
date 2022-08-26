from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class CreditsBalanceMessageComposer(MessageComposer):
    def __init__(self, creds: int):
        super().__init__()
        self.response = Response(outgoing.CreditsBalanceMessageComposer)
        self.credits = creds

    def compose(self):
        self.response.write_string(str(self.credits))
