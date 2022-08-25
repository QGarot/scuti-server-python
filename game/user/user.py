from game.user.details import Details


class User:
    def __init__(self):
        self.socket = None
        self.details = Details()

    def get_details(self) -> Details:
        return self.details
