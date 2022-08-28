class RoomUser:
    def __init__(self):
        self.entity = None
        self.virtual_id = 0
        self.last_chat_id = 0
        self.dance_id = 0
        self.x = 0
        self.y = 0
        self.z = 0
        # self.goal = Point(0, 0, 0)
        self.rotation = 0
        self.head_rotation = 0
        self.statuses = {}
        self.path = []
        self.path_cycle = None
        self.room = None
        self.is_walking = False
        self.needs_update = False
        self.is_loading_room = False
        self.chat_flood_timer = 0
        self.chat_count = 0
