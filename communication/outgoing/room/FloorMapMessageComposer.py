from communication.outgoing.message_composer import MessageComposer
from game.room.room import Room
from network.binary.response import Response
import communication.outgoing.header as outgoing


class FloorMapMessageComposer(MessageComposer):
    def __init__(self, room: Room):
        super().__init__()
        self.response = Response(outgoing.FloorMapMessageComposer)
        self.room = room

    def compose(self):
        self.response.write_bool(True)
        self.response.write_int(self.room.get_data().wall_height)
        self.response.write_string(self.room.get_model().floor_map)
