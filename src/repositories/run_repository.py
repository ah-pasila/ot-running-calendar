from entities.run import Run
from entities.user import User
from database_connection import get_database_connection


class Run_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_run(self, run):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO plans (day, description, length) VALUES (?, ?, ?)",
            (run.day, run.description, run.length)
        )

        self._connection.commit()

        return run

    def return_all_runs(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return list(rows)


run_repository = Run_repository(get_database_connection())
