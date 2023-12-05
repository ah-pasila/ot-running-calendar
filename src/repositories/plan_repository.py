from entities.plan import Plan
from entities.user import User
from database_connection import get_database_connection


class Plan_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_plan(self, day: str, description: str, length: int):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO plans (day, description, length) VALUES (?, ?)",
            (day, description, length)
        )

        self._connection.commit()

        return day, description, length

user_repository = Plan_repository(get_database_connection())
