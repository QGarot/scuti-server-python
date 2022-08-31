from utils.array import Matrix

VALID = 1
INVALID = 0


class RoomModel:
    def __init__(self, name: str, heightmap: str, door_x: int, door_y: int, door_z: float, door_rotation: int):
        self.name = name
        self.heightmap = heightmap
        self.door_x = door_x
        self.door_y = door_y
        self.door_z = door_z
        self.door_rotation = door_rotation

        self.map_size_x = None
        self.map_size_y = None
        self.squares = None
        self.square_height = None
        self.generate_heightmap_lookups()

        self.floor_map = None
        self.generate_relative_hp()

    def generate_heightmap_lookups(self):
        temporary = self.heightmap.split("{13}")
        self.map_size_x = len(temporary[0])
        self.map_size_y = len(temporary)

        self.squares = Matrix(self.map_size_x, self.map_size_y, 0)
        self.square_height = Matrix(self.map_size_x, self.map_size_y, 0)

        for y in range(self.map_size_y):
            line = temporary[y].replace(chr(10), "").replace(chr(13), "")
            x = 0
            for square in line:
                if square == "x":
                    if x == self.door_x and y == self.door_y:
                        self.squares.set(x, y, VALID)
                    else:
                        self.squares.set(x, y, INVALID)
                else:
                    self.squares.set(x, y, VALID)
                    self.square_height.set(x, y, RoomModel.parse(square))

                x = x + 1

    def generate_relative_heightmap(self):
        self.floor_map = self.heightmap.replace("{13}", chr(13))

    def generate_relative_hp(self):
        builder = ""
        for y in range(self.map_size_y):
            for x in range(self.map_size_x):
                if self.squares.get(x, y) == INVALID:
                    builder += "x"
                else:
                    builder += str(self.square_height.get(x, y))
            builder += chr(13)

        self.floor_map = builder

    @staticmethod
    def parse(square):

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

        return 0
