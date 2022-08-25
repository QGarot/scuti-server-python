import mysql.connector
from utils.logger import error


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
        Cette classe permet de gèrer les actions effectuées sur la base de données sélectionnée.
        :param host: Hôte du server MySQL
        :param user: Nom d'utilisateur
        :param password: Mot de passe
        :param name: Nom de la base de données
        """
        self.host = host
        self.user = user
        self.password = password
        self.name = name

        self.connection = None
        self.cursor = None

    def prepare_db(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=3306,
            user=self.user,
            database=self.name,
            password=self.password
        )

        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        self.cursor = None
        self.connection = None

    def update(self, table_name, attribute, new_value, sql_condition):
        """
        Permet de mettre à jour des données.
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

    def insert(self, table_name, structure, values):
        """
        Permet d'enregistrer des valeurs dans la table table_name.
        :param table_name: Nom de la table
        :param structure: Structure de la table
        :param values: Les attributs sous forme de liste ou de tuple
        :return: None
        """

        self.prepare_db()

        sql = "INSERT INTO " + table_name + " " + structure + " VALUES " + str(values)
        self.cursor.execute(sql)
        self.connection.commit()

        self.close_connection()

    def select(self, attributes, table_name, sql_condition=None) -> list:
        """
        Retourne une liste correspondant aux enregistrements retournés par la requête.
        Cette liste contient des n-uplets si n attributs sont sélectionnés dans la requête.
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
