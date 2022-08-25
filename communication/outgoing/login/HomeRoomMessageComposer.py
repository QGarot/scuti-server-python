from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response
import communication.outgoing.header as outgoing


class HomeRoomMessageComposer(MessageComposer):
    def __init__(self, room_id: int, force_enter: bool):
        super().__init__()
        self.response = Response(outgoing.HomeRoomMessageComposer)
        self.room_id = room_id
        self.force_enter = force_enter

    def compose(self):
        self.response.write_int(self.room_id)
        self.response.write_bool_int(self.force_enter)
