class RoomData:
    def __init__(self):
        self.id = -1
        self.type = ""
        self.owner_id = -1
        self.owner_name = ""
        self.name = ""
        self.state = 0
        self.password = ""
        self.thumbnail = ""
        self.users_now = 0
        self.users_max = 0
        self.description = ""
        self.trade_state = 0
        self.score = 0
        self.category = 0
        self.group_id = 0
        self.model = ""
        self.wall = ""
        self.floor = ""
        self.landscape = ""
        self.allow_pets = True
        self.allow_pets_eat = False
        self.allow_walk_through = False
        self.hide_wall = False
        self.wall_thickness = 0
        self.floor_thickness = 0
        self.wall_height = -1
        self.tags = []
        self.chat_type = 0
        self.chat_balloon = 0
        self.chat_speed = 0
        self.chat_max_distance = 0
        self.chat_flood_protection = 0
        self.who_can_mute = 1
        self.who_can_kick = 1
        self.who_can_ban = 1
