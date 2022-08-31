from communication.outgoing.message_composer import MessageComposer
from game.user.user import User
from network.binary.response import Response
import communication.outgoing.header as outgoing


class UserDisplayMessageComposer(MessageComposer):
    def __init__(self, entities: list):
        super().__init__()
        self.response = Response(outgoing.UserDisplayMessageComposer)
        self.entities = entities

    def compose(self):
        self.response.write_int(len(self.entities))
        for entity in self.entities:
            if type(entity == User):
                self.response.write_int(entity.get_details().id)
                self.response.write_string(entity.get_details().username)
                self.response.write_string(entity.get_details().motto)
                self.response.write_string(entity.get_details().figure)
                self.response.write_int(entity.get_room_user().virtual_id)  # virtual id
                self.response.write_int(entity.get_room_user().x)
                self.response.write_int(entity.get_room_user().y)
                self.response.write_string(str(entity.get_room_user().z))
                self.response.write_int(0)
                self.response.write_int(1)
                self.response.write_string(entity.get_details().gender.lower())
                self.response.write_int(-1)
                self.response.write_int(-1)
                self.response.write_int(0)
                self.response.write_int(0)  # achievement
                self.response.write_bool(False)
