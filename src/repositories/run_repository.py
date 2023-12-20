"""Class for saving data on planned runs and reading data from SQL database

ChatGPT was used to identify & solve problems related to return_all_runs printing
"""

from database_connection import get_database_connection


class Run_repository:

    def __init__(self, connection):
        self._connection = connection

        """Constructor of the class, sets up the connection to the database
        """

    def add_run(self, run): 
        """add_run adds planned run to the database: day, type, 
        duration, length, description, username
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO plans (day, type, duration, length, description, username)\
                VALUES (?, ?, ?, ?, ?, ?)",
            (run.day, run.run_type, run.duration,
             run.length, run.description, run.username)
        )

        self._connection.commit()

        return run

    def return_all_runs(self, given_username: str, datefrom: str, dateto: str):     
        """return_all_runs prints information on user's coming runs from given period 
        or if no period is given, then all runs from today on
        """
        cursor = self._connection.cursor()
        if dateto == "":
            cursor.execute("SELECT * FROM plans WHERE username = ? AND day >= date('now')",
                           (given_username,)
                           )
            rows = cursor.fetchall()
# Starting point: the code below (4 rows) was partly created by ChatGPT
            result = []
            for row in rows:
                result.append(
                    f"date: {row[1]}, effort: {row[2]}, duration and length:\
                        {row[3]} min, {row[4]} km")
            return '\n'.join(result)
# Ending point point: the code above (4 rows) was partly created by ChatGPT

        else:
            cursor.execute("SELECT * FROM plans WHERE username = ? AND day >= ? AND day <= ?",
                           (given_username, datefrom, dateto,)
                           )
            rows = cursor.fetchall()

# Starting point: the code below (4 rows) was partly created by ChatGPT
            result = []
            for row in rows:
                result.append(
                    f"date: {row[1]}, effort: {row[2]}, duration and length:\
                        {row[3]} min, {row[4]} km")
            return '\n'.join(result)
# Ending point point: the code above (4 rows) was partly created by ChatGPT


    def return_run_count(self, given_username: str, datefrom: str, dateto: str):
        """return_run_count returns the total number of user's runs from given period,
        or if no period is given, then all runs
        """
        if dateto == "":
            cursor = self._connection.cursor()
            res = cursor.execute("SELECT * FROM plans WHERE username = ? AND day >= date('now')",
                                 (given_username,)
                                 )
            return (len(res.fetchall()))
        else:
            cursor = self._connection.cursor()
            res = cursor.execute("SELECT * FROM plans WHERE username = ?\
                                 AND day >= ? AND day <= ?",
                                 (given_username, datefrom, dateto,)
                                 )
            return (len(res.fetchall()))


    def return_run_count_in_db(self):
        """return_run_count returns the total number of runs in the database 
        """
        cursor = self._connection.cursor()
        res = cursor.execute("SELECT * FROM plans"
                             )
        return (len(res.fetchall()))

    def return_run_sum_min(self, given_username: str, datefrom: str, dateto: str):
        """return_run_sum_min returns the total sum of user's running minutes 
        from coming runs from given period or if no period is given, 
        then all runs from today on
        """
        cursor = self._connection.cursor()
        if dateto == "":
            res = cursor.execute("SELECT SUM(duration) FROM plans WHERE username = ?\
                                 AND day >= date('now')",
                                 (given_username,)
                                 )
            total_sum = res.fetchone()[0]
            return total_sum
        else:
            res = cursor.execute("SELECT SUM(duration) FROM plans WHERE username = ?\
                                 AND day >= ? AND day <= ?",
                                 (given_username, datefrom, dateto,)
                                 )
            total_sum = res.fetchone()[0]
            return total_sum


    def return_run_sum_min_types(self, given_username: str, given_type: int, \
                                 datefrom: str, dateto: str):
        """return_run_sum_min returns the total sum of user's running minutes 
        by run type from coming runs from given period or if no period is given, 
        then all runs from today on
        """
        cursor = self._connection.cursor()
        if dateto == "":
            res = cursor.execute("SELECT SUM(duration) FROM plans \
                                 WHERE username = ? AND type = ? AND day >= date('now')",
                                 (given_username, given_type,)
                                 )
            total_sum = res.fetchone()[0]
            return total_sum
        else:
            res = cursor.execute("SELECT SUM(duration) FROM plans\
                                 WHERE username = ? AND type = ? AND day >= ? AND day <= ?",
                                 (given_username, given_type, datefrom, dateto,)
                                 )
            total_sum = res.fetchone()[0]
            return total_sum

    def return_run_sum_km(self, given_username: str, datefrom: str, dateto: str):
        """return_run_sum_km returns the total sum of user's running kilometers 
        from coming runs from given period or if no period is given, then all runs 
        from today on
        """
        cursor = self._connection.cursor()
        if dateto == "":
            res = cursor.execute("SELECT SUM(length) FROM plans WHERE username = ?\
                                 AND day >= date('now')",
                                 (given_username,)
                                 )
            total_sum = res.fetchone()[0]
            return total_sum
        else:
            res = cursor.execute("SELECT SUM(length) FROM plans WHERE username = ?\
                                 AND day >= ? AND day <= ?",
                                 (given_username, datefrom, dateto,)
                                 )
            total_sum = res.fetchone()[0]
            return total_sum


    def remove_run(self, given_username: str, removedate):
        """remove_run removes user's run(s) from a given day
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM plans WHERE username = ? AND day = ?",
            (given_username, removedate,)
        )

        self._connection.commit()

    def remove_all_runs(self):
        """remove_all_runs removes all runs from database
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM plans",
        )

        self._connection.commit()


run_repository = Run_repository(get_database_connection())
