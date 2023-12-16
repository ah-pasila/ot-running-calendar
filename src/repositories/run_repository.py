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
            "INSERT INTO plans (day, type, duration, length, username) VALUES (?, ?, ?, ?, ?)",
            (run.day, run.type, run.duration, run.length, run.username)
        )

        self._connection.commit()

        return run
    

    def return_all_runs(self, given_username: str):
        cursor = self._connection.cursor()
        cursor.execute("select * from plans where username = ? and day > date('now')",
                       (given_username,)
        )
        rows = cursor.fetchall()
        for row in rows:
            print("date: ", row[1], " effort: ", row[2], " duration and length: ", row[3], " min ", row[4], " km")
       
    def return_run_count(self, given_username: str):
        cursor = self._connection.cursor()
        res = cursor.execute("select * from plans where username = ?",
                             (given_username,)
        )
        return (len(res.fetchall()))
    
    def return_run_sum_min(self, given_username: str):
        cursor = self._connection.cursor()
        res = cursor.execute("select sum(duration) from plans where username = ? and day > date('now')",
                             (given_username,)
        )
        total_sum = res.fetchone()[0]
        return total_sum
    
    def return_run_sum_min_types(self, given_username: str, given_type: int):
        cursor = self._connection.cursor()
        res = cursor.execute("select sum(duration) from plans where username = ? and type = ? and day > date('now')",
                             (given_username, given_type,)
        )
        total_sum = res.fetchone()[0]
        return total_sum

    def return_run_sum_km(self, given_username: str):
        cursor = self._connection.cursor()
        res = cursor.execute("select sum(length) from plans where username = ? and day > date('now')",
                             (given_username,)
        )
        total_sum = res.fetchone()[0]
        return total_sum
    
    def return_all_runs_period(self, given_username: str, datefrom, dateto):
        cursor = self._connection.cursor()
        cursor.execute("select * from plans where username = ? and day >= ? and day <= ?",
                       (given_username, datefrom, dateto,)
        )
        rows = cursor.fetchall()
        for row in rows:
            print("date: ", row[1], " effort: ", row[2], " duration and length: ", row[3], " min ", row[4], " km")

    def return_run_count_period(self, given_username: str, datefrom: str, dateto: str):
        cursor = self._connection.cursor()
        res = cursor.execute("select * from plans where username = ? and day >= ? and day <= ?",
                             (given_username, datefrom, dateto,)
        )
        return (len(res.fetchall()))
    
    def return_run_sum_min_period(self, given_username: str, datefrom: str, dateto: str):
        cursor = self._connection.cursor()
        res = cursor.execute("select sum(duration) from plans where username = ? and day >= ? and day <= ?",
                             (given_username, datefrom, dateto,)
        )
        total_sum = res.fetchone()[0]
        return total_sum
    
    def return_run_sum_min_types_period(self, given_username: str, given_type: int, datefrom: str, dateto: str):
        cursor = self._connection.cursor()
        res = cursor.execute("select sum(duration) from plans where username = ? and type = ? and day >= ? and day <= ?",
                             (given_username, given_type, datefrom, dateto,)
        )
        total_sum = res.fetchone()[0]
        return total_sum

    def return_run_sum_km_period(self, given_username: str, datefrom: str, dateto: str):
        cursor = self._connection.cursor()
        res = cursor.execute("select sum(length) from plans where username = ? and day >= ? and day <= ?",
                             (given_username, datefrom, dateto,)
        )
        total_sum = res.fetchone()[0]
        return total_sum

run_repository = Run_repository(get_database_connection())
