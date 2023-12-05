# Kysytty ChatGPT:ltä neuvoa koodin toimimattomuuteen

from entities.user import User
from database_connection import get_database_connection

class User_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (user.username, user.password)
        )

        self._connection.commit()

        return user.username, user.password


user_repository = User_repository(get_database_connection())
