import communication.outgoing.header as outgoing
from communication.outgoing.message_composer import MessageComposer
from network.binary.response import Response


class RoomModelMessageComposer(MessageComposer):
    def __init__(self, model_name: str, room_id: int):
        super().__init__()
        self.response = Response(outgoing.InitialRoomInfoMessageComposer)
        self.model_name = model_name
        self.room_id = room_id

    def compose(self):
        self.response.write_string(self.model_name)
        self.response.write_int(self.room_id)
