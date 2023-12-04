from entities.user import User
from database_connection import get_database_connection

class User_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?,?)",
            (user.username, user.password)
        )
        
        self._connection.commit()

user_repository = User_repository(get_database_connection())