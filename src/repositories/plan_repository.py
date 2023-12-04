from entities.plan import plan
from entities.user import user
from database_connection import get_database_connection

class Plan_repository:
    def __init__(self, connection):
        self._connection = connection

    def add_plan(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into plans (username, password) values (?,?)",
            (user.username, user.password)
        )
        
        self._connection.commit()
 
user_repository = User_repository(get_database_connection())