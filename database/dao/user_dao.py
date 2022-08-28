from database.database import Database
from game.user.user import User


class UserDao:

    @staticmethod
    def authenticate(user: User, sso_ticket) -> bool:
        """
        Return true if : user with SSO Ticket is found. Then user is completly filled with corresponding data.
        """
        select = Database.get_instance().select(attributes="id, username, rank, mission, figure, credits",
                                                table_name="users",
                                                sql_condition="sso_ticket='"+sso_ticket+"'")

        if len(select) == 1:
            user.fill_data(select[0])
            return True
        else:
            return False
