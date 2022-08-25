from communication.message_handler import MessageHandler
from network.server import Server


class Scuti:
    def __init__(self):
        self.server = None
        self.load()

    @staticmethod
    def load():
        MessageHandler().get_instance()

    def run(self, host: str, port: int):
        self.server = Server(host, port)
        print(">> Server on!")
