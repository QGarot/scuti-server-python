from communication.outgoing.message_composer import MessageComposer
from game.user.user import User
from network.binary.response import Response
import communication.outgoing.header as outgoing


class UserStatusMessageComposer(MessageComposer):
    def __init__(self, entities: list):
        super().__init__()
        self.response = Response(outgoing.UserStatusMessageComposer)
        self.entities = entities

    def compose(self):
        self.response.write_int(len(self.entities))

        for entity in self.entities:
            if type(entity) == User:
                self.response.write_int(entity.get_room_user().virtual_id)
                self.response.write_int(entity.get_room_user().x)
                self.response.write_int(entity.get_room_user().y)
                self.response.write_string(str(entity.get_room_user().z))
                self.response.write_int(6)
                self.response.write_int(1)

                print(entity.get_room_user().y, entity.get_room_user().rotation)

                status = "/"

                for key, value in entity.get_room_user().statuses.items():
                    status += key + " " + value + "/"

                self.response.write_string(status + "/")

                print("ok stp enft")
