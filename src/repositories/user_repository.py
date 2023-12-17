"""In this class, ChatGPT was used to find out reasons why code was not working
"""

from entities.user import User
from database_connection import get_database_connection
from werkzeug.security import generate_password_hash, check_password_hash


class User_repository:

    """Class for saving user data and reading user data from SQL database
    """
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

    def check_username_exists(self, given_username):
        cursor = self._connection.cursor()
        res = cursor.execute("select username from users where username = ?",
                       (given_username,)
        )
        returning_username = res.fetchone()
        if returning_username and given_username == returning_username[0]:
            return True
        else:
            return False

    """In the check_username_exists method, ChatGPT was used to formulate the if & return parts properly"""

    def check_password_correct(self, given_username, given_password):
        cursor = self._connection.cursor()
        res = cursor.execute("select password from users where username = ?",
                       (given_username,)
        )       
        returning_password = res.fetchone()
        if returning_password and check_password_hash(returning_password[0], given_password):
            return True
        else:
            return False

    def return_age(self, given_username):
        cursor = self._connection.cursor()
        res = cursor.execute("select age from users where username = ?",
                       (given_username,)
        )       
        returning_age = res.fetchone()
        return returning_age[0]

    def return_user_count(self):
        cursor = self._connection.cursor()
        cursor.execute("select count(*) from users")
        return (len(cursor.fetchall()))

    def remove_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM users",
        )

        self._connection.commit()

user_repository = User_repository(get_database_connection())
