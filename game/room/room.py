from game.room.room_data import RoomData


class Room:
    def __init__(self, data: RoomData):
        self.room_data = data
        self.model = None
        self.mapping = None

    def get_data(self) -> RoomData:
        return self.room_data
