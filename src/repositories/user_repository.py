"""
Class for saving user data and reading user data from SQL database

ChatGPT was used to find out reasons why code was not working in this class
"""

from werkzeug.security import generate_password_hash, check_password_hash
from database_connection import get_database_connection


class UserRepository:

    def __init__(self, connection):
        """Constructor of the class, sets up the connection to the database
        """
        self._connection = connection

    def add_user(self, user):
        """add_user adds user info to the database: username, password, gender, age.
        Before adding to the database, password is hashed.
        """
        password = generate_password_hash(user.password)
        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO users (username, password, gender, age) VALUES (?, ?, ?, ?)',
            (user.username, password, user.gender, user.age)
        )

        self._connection.commit()

        return user


    def check_username_exists(self, given_username):
        """check_username_exists checks that given username can be found from the database
        """
        cursor = self._connection.cursor()
        res = cursor.execute("SELECT username FROM users WHERE username = ?",
                             (given_username,)
                             )
        returning_username = res.fetchone()
        if returning_username and given_username == returning_username[0]:
            return True
        else:
            return False


    def check_password_correct(self, given_username, given_password):
        """check_password_correct checks that given username and password combination is valid
        Because password is in hashed form, check_password_hash must be used to compare passwords
        """
        cursor = self._connection.cursor()
        res = cursor.execute("SELECT password FROM users WHERE username = ?",
                             (given_username,)
                             )
        returning_password = res.fetchone()
        if returning_password and check_password_hash(returning_password[0], given_password):
            return True
        else:
            return False

    def return_age(self, given_username):
        """return_age returns the age of the given user
        """
        cursor = self._connection.cursor()
        res = cursor.execute("SELECT age FROM users WHERE username = ?",
                             (given_username,)
                             )
        returning_age = res.fetchone()
        return returning_age[0]


    def return_user_count(self):
        """return_user_count returns the total number of the users in the database
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        return (len(cursor.fetchall()))


    def remove_all_users(self):
        """remove_all_users removes all users from database
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM users",
        )

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
