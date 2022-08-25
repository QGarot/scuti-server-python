from typing import Optional

from game.user.user import User


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User) -> None:
        user_id = user.get_details().id
        if user_id not in self.users:
            self.users[user_id] = user

    def get_users_connected(self):
        return self.users.values()

    def get_user_by_id(self, user_id: int) -> User:
        if user_id in self.get_users_connected():
            return self.users.get(user_id)
        else:
            # todo: dao search
            pass

    def get_user_by_socket(self, socket) -> Optional[User]:
        for user in self.get_users_connected():
            if user.socket == socket:
                return user
        return None
