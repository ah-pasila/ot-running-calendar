# Luokan typoista ja ongelmista kysytty neuvoa chatGPT:ltä ja korjailtu virheitä tämän perusteella

from entities.user import User
from entities.run import Run
from entities.run_plan import RunPlan
from repositories.user_repository import (
    User_repository as default_user_repository
)

from repositories.run_repository import (
    Run_repository as default_run_repository
)


class Run_calendar_service:

    def __init__(
        self,
        user_repository=default_user_repository,
        run_repository=default_run_repository
    ):
        self._user_repository = user_repository
        self._plan_repository = run_repository

    def add_user(self, username: str, password: str, gender: str, age: int):
        user = User(username, password, gender, age)
        return self._user_repository.add_user(self, user, gender, age)
    
    def add_run(self, day: str, description: str, length: int):
        run = Run(day, description, length)
        return self._run_repository.add_run(self, run)


run_calendar_service = Run_calendar_service()
