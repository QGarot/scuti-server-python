from communication.outgoing.message_composer import MessageComposer
from game.room.room_model import RoomModel
from network.binary.response import Response
import communication.outgoing.header as outgoing


class HeightMapMessageComposer(MessageComposer):
    def __init__(self, room_model: RoomModel):
        super().__init__()
        self.response = Response(outgoing.HeightMapMessageComposer)
        self.room_model = room_model

    def compose(self):

        self.response.write_int(self.room_model.map_size_x)
        self.response.write_int(self.room_model.map_size_x * self.room_model.map_size_y)

        for y in range(self.room_model.map_size_y):
            for x in range(self.room_model.map_size_x):
                self.response.write_short(int(self.room_model.square_height[y][x] * 256))
