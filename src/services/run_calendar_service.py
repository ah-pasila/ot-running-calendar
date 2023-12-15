""" ChatGPT was used to find typos and problemts from the code.
"""

from entities.user import User
from entities.run import Run
from entities.run_plan import RunPlan
from repositories.user_repository import (
    user_repository as default_user_repository
)

from repositories.run_repository import (
    run_repository as default_run_repository
)
from werkzeug.security import check_password_hash

class Run_calendar_service:

    """Class for creating Run calendar service
        Args: 
            user_repository: class responsible for data operations related to user
            run_repository: class responsible for data operations related to user
    """

    def __init__(
        self,
        user_repository=default_user_repository,
        run_repository=default_run_repository
    ):
        self._user_repository = user_repository
        self._run_repository = run_repository
        self.current_user = User("","","","")

    def add_user(self, username: str, password: str, gender: str, age: int):
        user = User(username, password, gender, age)
        print(user.password)
        return self._user_repository.add_user(user)

    def login_user(self, given_username: str, given_password: str):
        if self._user_repository.return_username(given_username) == True:
            hashed_password = self._user_repository.return_password(given_username)
            if check_password_hash(hashed_password, given_password):
                self.current_user = User(given_username, "", "", "")
                return True
            else:
                return False
        else: 
            return False

    def add_run(self, day: str, description: str, length: int, username: str):
        username = self.current_user.username
        run = Run(day, description, length, username)
        return self._run_repository.add_run(run)
    
    def print_runs(self):
        return self._run_repository.return_all_runs()

run_calendar_service = Run_calendar_service()
