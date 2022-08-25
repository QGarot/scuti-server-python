from game.user.user import User
from game.user.user_manager import UserManager
from utils.message_treatment import parse
from asyncore import dispatcher_with_send

from communication.message_handler import MessageHandler


class Connection(dispatcher_with_send):

    def __init__(self, sock):
        super().__init__(sock)
        self.user = User(self.socket)

    def handle_read(self):
        data = self.recv(4)
        if data:
            header, request = parse(data, self)
            MessageHandler.get_instance().handle(self.user, header, request)
        else:
            self.socket.close()
