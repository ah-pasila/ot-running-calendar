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

    def add_user(self, username: str, password: str, gender: str, age: int):
        user = User(username, password, gender, age)
        return self._user_repository.add_user(user)

    def add_run(self, day: str, description: str, length: int):
        run = Run(day, description, length)
        return self._run_repository.add_run(run)
    
    def print_runs(self):
        return self._run_repository.return_all_runs()

run_calendar_service = Run_calendar_service()
