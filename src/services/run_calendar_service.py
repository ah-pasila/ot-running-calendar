#Luokan typoista ja ongelmista kysytty neuvoa chatGPT:ltä

from entities.plan import Plan
from entities.user import User
from entities.run_calendar import Run_calendar
from datetime import date

class Run_calendar_service:

    def __init__(self):
        self.user = User("test1", "test2")
        self.run_plan = Plan()
        self.running_calendar = Run_calendar()

    def add_run(self, day: str, description:str, length: str):
        self.run_plan.add_run(day = day, description = description, length = length)

    def add_username(self, name: str):
        self.user.add_username(username = name)

    def add_password(self, password: str):
        self.user.add_password(password = password)

    def add_gender(self, gender: str):
        self.user.add_gender(gender = gender)

    def add_age(self, age: int):
        self.user.add_age(age = age)

    def print_runs(self):
        self.run_plan.print_runs()

    def print_current_month_calendar(self):
        self.running_calendar.print_current_month_calendar()

    def print_next_month_calendar(self):
        self.running_calendar.print_next_month_calendar()