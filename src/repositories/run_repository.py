from entities.run import Run
from entities.user import User
from database_connection import get_database_connection


class Run_repository:

    """Class for saving run data and reading run data from SQL database
    """
    def __init__(self, connection):
        self._connection = connection

    def add_run(self, run):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO plans (day, description, length, username) VALUES (?, ?, ?, ?)",
            (run.day, run.description, run.length, run.username)
        )

        self._connection.commit()

        return run

    def return_all_runs(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from plans")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3])
       
    def return_run_count(self):
        cursor = self._connection.cursor()
        cursor.execute("select count(*) from plans")
        return (len(cursor.fetchall()))


run_repository = Run_repository(get_database_connection())
