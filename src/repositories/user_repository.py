# Kysytty ChatGPT:ltä neuvoa koodin toimimattomuuteen

from entities.user import User
from database_connection import get_database_connection


class User_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, username: str, password: str):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        self._connection.commit()

        return username, password


user_repository = User_repository(get_database_connection())
