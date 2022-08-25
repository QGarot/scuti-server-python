from communication.message_handler import MessageHandler
from database.database import Database
from game.user.user_manager import UserManager
from network.server import Server
from utils.logger import info


class Scuti:
    def __init__(self):
        self.server = None

        self.display_about()
        self.load()

    @staticmethod
    def display_about():
        print("~ Scuti Project ~")
        print("Tig3r & KOZEN")
        print("")

    @staticmethod
    def load():
        MessageHandler().get_instance()
        info("Message handler loaded!")

        Database.get_instance()
        info("Database loaded!")

        UserManager.get_instance()
        info("User loaded!")

    def run(self, host: str, port: int):
        self.server = Server(host, port)
        print(">> Server on!")
