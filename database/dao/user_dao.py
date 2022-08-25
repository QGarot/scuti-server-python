from database.database import Database
from game.user.user import User


class UserDao:

    @classmethod
    def authenticate(cls, user: User, sso_ticket) -> bool:
        """
        Return true if : SSO Ticket is found and user is completly filled with corresponding data.
        """
        select = Database.get_instance().select(attributes="id, username, rank, mission, figure, credits",
                                                table_name="users",
                                                sql_condition="sso_ticket='"+sso_ticket+"'")

        if len(select) == 1:
            cls.fill_data(user, select[0])
            return True
        else:
            return False

    @classmethod
    def fill_data(cls, user: User, row):
        """
        Fill user details thanks to row, get with SQL query
        """
        user.details.id = row[0]
        user.details.username = row[1]
        user.details.motto = row[3]
        user.details.figure = row[4]
        user.details.rank = row[2]
        user.details.credits = row[5]
