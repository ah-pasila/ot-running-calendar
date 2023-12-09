# Kysytty ChatGPT:ltä neuvoa koodin toimimattomuuteen

from entities.user import User
from database_connection import get_database_connection
from werkzeug.security import generate_password_hash


class User_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, user):
        password = generate_password_hash(user.password)
        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO users (username, password, gender, age) VALUES (?, ?, ?, ?)',
            (user.username, password, user.gender, user.age)
        )

        self._connection.commit()

        return user


user_repository = User_repository(get_database_connection())
