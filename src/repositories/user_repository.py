"""In this class, ChatGPT was used to find out reasons why code was not working
"""

from entities.user import User
from database_connection import get_database_connection
from werkzeug.security import generate_password_hash


class User_repository:

    """Class for saving user data and reading user data from SQL database
    """
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, user):
#        password = generate_password_hash(user.password)
        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO users (username, password, gender, age) VALUES (?, ?, ?, ?)',
            (user.username, user.password, user.gender, user.age)
        )

        self._connection.commit()

        return user
    
    def return_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username = ?",
                       (username,)
        )
        row = cursor.fetchone()
        returning_username = row[1]
        return returning_username
    
    def return_password(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username = ?",
                       (username,)
        )
        row = cursor.fetchone()
        returning_password = row[1]
        return returning_password

    def return_user_count(self):
        cursor = self._connection.cursor()
        cursor.execute("select count(*) from users")
        return (len(cursor.fetchall()))

user_repository = User_repository(get_database_connection())
