from game.room.room_data import RoomData


class Room:
    def __init__(self):
        self.room_data = None

    def get_data(self) -> RoomData:
        return self.room_data
