from enum import Enum


class SquareState(Enum):
    OPEN = 0
    CLOSED = 1


class RoomModel:
    def __init__(self, name: str, heightmap: str, door_x: int, door_y: int, door_z: int, door_rot: int):
        self.name = name
        self.heightmap = heightmap
        self.door_x = door_x
        self.door_y = door_y
        self.door_z = door_z
        self.door_rot = door_rot

        self.map_size_x = None
        self.map_size_y = None
        self.squares = None

    def generate_heightmap_lookups(self):
        temporary = self.heightmap.split("{13}")

        self.map_size_x = len(temporary[0])
        self.map_size_y = len(temporary)

        self.squares = []

        for y in range(self.map_size_y):
            line = temporary[y]
            line = line.replace(chr(10), "")
            line = line.replace(chr(13), "")

            self.squares.append([])
            x = 0
            for square in line:
                if square == "x":
                    self.squares[y].append(SquareState.CLOSED)
                else:
                    self.squares[y].append(SquareState.OPEN)

                # TODO: door

                x = x + 1


