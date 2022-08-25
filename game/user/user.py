from game.user.details import Details


class User:
    def __init__(self, socket):
        self.socket = socket
        self.details = Details()

    def get_details(self) -> Details:
        """
        Get details
        :return:
        """
        return self.details
