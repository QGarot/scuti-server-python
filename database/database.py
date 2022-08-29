import mysql.connector


class Database:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Database("localhost", "root", "", "icarusdb")
            cls.instance.prepare_db()
            cls.instance.close_connection()

        return cls.instance

    def __init__(self, host, user, password, name):
        """
        This class allows to manage actions on database selected
        :param host:
        :param user:
        :param password:
        :param name:
        """
        self.host = host
        self.user = user
        self.password = password
        self.name = name

        self.connection = None
        self.cursor = None

    def prepare_db(self):
        """
        Connect to database and get cursor. This method must be called before each action on database.
        :return:
        """
        self.connection = mysql.connector.connect(
            host=self.host,
            port=3306,
            user=self.user,
            database=self.name,
            password=self.password
        )

        self.cursor = self.connection.cursor()

    def close_connection(self):
        """
        Close connection and cursor. This method must be called after each action on database.
        :return:
        """
        self.cursor.close()
        self.connection.close()
        self.cursor = None
        self.connection = None

    def update(self, table_name, attribute, new_value, sql_condition):
        """
        Update data
        :param table_name:
        :param attribute:
        :param new_value:
        :param sql_condition:
        :return:
        """
        self.prepare_db()

        sql = "UPDATE " + table_name + " SET " + attribute + " = '" + new_value + "' WHERE " + sql_condition
        self.cursor.execute(sql)
        self.connection.commit()

        self.close_connection()

    def update2(self, table_name: str, attributes: dict, sql_condition: str):
        """
        Update table name.
        Example of attributes: {"name": "Tig3r"}
        -> {"fied": new value of this field}
        :param table_name:
        :param attributes:
        :param sql_condition:
        :return:
        """
        attr_str = ""
        first = True
        for couple in attributes.items():
            print(couple)
            if first:
                attr_str = attr_str + couple[0] + " = '" + str(couple[1]) + "'"
                first = False
            else:
                attr_str = attr_str + ", " + couple[0] + " = '" + str(couple[1]) + "'"

        self.prepare_db()
        sql = "UPDATE " + table_name + " SET " + attr_str + " WHERE " + sql_condition
        self.cursor.execute(sql)
        self.connection.commit()

        self.close_connection()

    def insert(self, table_name, structure, values):
        """
        Save data.
        :param table_name:
        :param structure:
        :param values:
        :return: None
        """

        self.prepare_db()

        sql = "INSERT INTO " + table_name + " " + structure + " VALUES " + str(values)
        self.cursor.execute(sql)
        self.connection.commit()

        self.close_connection()

    def select(self, attributes, table_name, sql_condition=None) -> list:
        """
        Return a list of n-tuple if n fields are selected
        :param sql_condition:
        :param table_name:
        :param attributes:
        :return: list
        """
        self.prepare_db()

        if sql_condition is not None:
            sql = "SELECT " + attributes + " FROM " + table_name + " WHERE " + sql_condition
        else:
            sql = "SELECT " + attributes + " FROM " + table_name
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        self.close_connection()
        return result
