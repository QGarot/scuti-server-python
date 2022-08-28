from enum import Enum


class SquareState(Enum):
    OPEN = 0
    CLOSED = 1


class RoomModel:
    def __init__(self, name: str, heightmap: str, door_x: int, door_y: int, door_z: float, door_rot: int):
        self.name = name
        self.heightmap = heightmap
        self.door_x = door_x
        self.door_y = door_y
        self.door_z = door_z
        self.door_rot = door_rot

        self.map_size_x = None
        self.map_size_y = None

        # State (OPEN or CLOSE, cf. enum class SquareState) of each square
        self.squares = None

        # Height (int) of each square
        self.square_height = None

        self.generate_heightmap_lookups()

    def generate_heightmap_lookups(self) -> None:
        """
        Generate squares & square_height arrays thanks to heightmap
        :return:
        """
        temporary = self.heightmap.split("{13}")

        self.map_size_x = len(temporary[0])
        self.map_size_y = len(temporary)

        self.squares = []
        self.square_height = []

        for y in range(self.map_size_y):
            line = temporary[y]
            line = line.replace(chr(10), "")
            line = line.replace(chr(13), "")

            self.squares.append([])
            self.square_height.append([])
            x = 0
            for square in line:
                if square == "x":
                    self.squares[y].append(SquareState.CLOSED)
                    self.square_height[y].append(0)
                else:
                    self.squares[y].append(SquareState.OPEN)
                    self.square_height[y].append(self.parse(square))

                if x == self.door_x and y == self.door_y:
                    self.squares[y][x] = SquareState.OPEN
                    self.square_height[y][x] = self.door_z

                x = x + 1

    def generate_relative_heightmap(self) -> None:
        pass

    @staticmethod
    def parse(square: str):

        if square == "0":
            return 0
        if square == "1":
            return 1
        if square == "2":
            return 2
        if square == "3":
            return 3
        if square == "4":
            return 4
        if square == "5":
            return 5
        if square == "6":
            return 6
        if square == "7":
            return 7
        if square == "8":
            return 8
        if square == "9":
            return 9
        if square == "a":
            return 10
        if square == "b":
            return 11
        if square == "c":
            return 12
        if square == "d":
            return 13
        if square == "e":
            return 14
        if square == "f":
            return 15
        if square == "g":
            return 16
        if square == "h":
            return 17
        if square == "i":
            return 18
        if square == "j":
            return 19
        if square == "k":
            return 20
        if square == "l":
            return 21
        if square == "m":
            return 22
        if square == "n":
            return 23
        if square == "o":
            return 24
        if square == "p":
            return 25
        if square == "q":
            return 26
        if square == "r":
            return 27
        if square == "s":
            return 28
        if square == "t":
            return 29
        if square == "u":
            return 30
        if square == "v":
            return 31
        if square == "w":
            return 32

        return -1
