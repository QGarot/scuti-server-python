class Details:

    def __init__(self):
        self.id = -1
        self.username = ""
        self.motto = ""
        self.figure = ""
        self.rank = 1
        self.credits = 0
        self.machine_id = ""
        self.authenticated = False
        self.gender = ""

    def fill_details(self, user_id, username, motto, figure, rank, credits, gender):
        """
        Fill data
        :param gender:
        :param user_id:
        :param username:
        :param motto:
        :param figure:
        :param rank:
        :param credits:
        :return:
        """
        self.id = user_id
        self.username = username
        self.motto = motto
        self.figure = figure
        self.rank = rank
        self.credits = credits
        self.gender = gender

    def get_user_object(self):
        pass