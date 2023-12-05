# Luokan typoista ja ongelmista kysytty neuvoa chatGPT:ltä ja korjailtu virheitä tämän perusteella

from entities.user import User
from entities.plan import Plan
from entities.run_calendar import Run_calendar
from repositories.user_repository import (
    User_repository as default_user_repository
)

from repositories.plan_repository import (
    Plan_repository as default_plan_repository
)


class Run_calendar_service:

    def __init__(
        self,
        user_repository=default_user_repository,
        plan_repository=default_plan_repository
    ):
        self.run_plan = Plan()
        self.running_calendar = Run_calendar()
        self._user_repository = user_repository
        self._plan_repository = plan_repository

    def add_run(self, day: str, description: str, length: int):
        return self._plan_repository.add_plan(self, day=day, description=description, length=length)

    def add_user(self, username: str, password: str):
        user = User(username, password)
        return self._user_repository.add_user(self, user)

    def add_gender(self, gender: str):
        self.user.add_gender(gender=gender)

    def add_age(self, age: int):
        self.user.add_age(age=age)

    def print_runs(self):
        self.run_plan.print_runs()

    def print_current_month_calendar(self):
        self.running_calendar.print_current_month_calendar()

    def print_next_month_calendar(self):
        self.running_calendar.print_next_month_calendar()


run_calendar_service = Run_calendar_service()
