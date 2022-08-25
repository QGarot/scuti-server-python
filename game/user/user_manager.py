from typing import Optional

from database.dao.user_dao import UserDao
from game.user.user import User


class UserManager:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = UserManager()
        return cls.instance

    def __init__(self):
        self.users = {}

    def add_user(self, user: User) -> None:
        user_id = user.get_details().id
        if user_id not in self.users:
            self.users[user_id] = user

    def disconnect(self, user: User) -> None:
        user_id = user.get_details().id
        if user_id in self.users:
            user.socket.close()
            self.users.pop(user_id)

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

    def authenticate_user(self, user: User, sso_ticket: str):
        if UserDao.authenticate(user, sso_ticket):
            self.add_user(user)
            print("TOUUUUT FONCTIONNE STP")
        else:
            user.socket.close()
