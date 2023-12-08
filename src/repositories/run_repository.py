from entities.run import Run
from entities.user import User
from database_connection import get_database_connection


class Run_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_run(self, day: str, description: str, length: int):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO plans (day, description, length) VALUES (?, ?)",
            (day, description, length)
        )

        self._connection.commit()

        return day, description, length


run_repository = Run_repository(get_database_connection())
