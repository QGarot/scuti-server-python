from utils.message_treatment import parse
from asyncore import dispatcher_with_send

from communication.message_handler import MessageHandler


class EchoHandler(dispatcher_with_send):

    def handle_read(self):
        data = self.recv(4)
        if data:
            header, request = parse(data, self)
            MessageHandler.get_instance().handle(None, header, request)
        else:
            self.socket.close()
