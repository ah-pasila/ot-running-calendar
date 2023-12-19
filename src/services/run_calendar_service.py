""" ChatGPT was used to find typos and problemts from the code.
"""

from entities.user import User
from entities.run import Run
from repositories.user_repository import (
    user_repository as default_user_repository
)

from repositories.run_repository import (
    run_repository as default_run_repository
)

class RunCalendarService:

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
        self.login_status = False

    def add_user(self, username: str, password: str, gender: str, age: int):
        user = User(username, password, gender, age)
        return self._user_repository.add_user(user)

    def login_user(self, given_username: str, given_password: str):
        if self.check_username(given_username) == True and self._user_repository.check_password_correct(given_username, given_password):
            self.login_status = True
            self.current_user = User(given_username, "", "", "")
            return True
        else:
            return False

    def logout_user(self):
        self.login_status = False

    def check_username(self, given_username):
        if self._user_repository.check_username_exists(given_username) == True: 
            return True
        else:
            return False

    def add_run(self, day: str, type: str, duration: str, length: int, description: str, username: str):
        username = self.current_user.username
        run = Run(day, type, duration, length, description, username)
        return self._run_repository.add_run(run)
    
    def remove_run(self, day: str):
        self._run_repository.remove_run(day)
    
    def return_all_runs(self):
        username = self.current_user.username
        return self._run_repository.return_all_runs(username)
    
    def return_number_of_runs(self):
        username = self.current_user.username
        return self._run_repository.return_run_count(username)

    def return_sum_of_runs_min(self):
        username = self.current_user.username
        return self._run_repository.return_run_sum_min(username)
    
    def return_sum_of_runs_min_type(self, type: int):
        username = self.current_user.username
        type = type
        return self._run_repository.return_run_sum_min_types(username, type)

    def return_sum_of_runs_km(self):
        username = self.current_user.username
        return self._run_repository.return_run_sum_km(username)

    def return_all_runs_period(self, datefrom: str, dateto: str):
        username = self.current_user.username
        return self._run_repository.return_all_runs_period(username, datefrom, dateto)

    def return_number_of_runs_period(self, datefrom: str, dateto: str):
        username = self.current_user.username
        return self._run_repository.return_run_count_period(username, datefrom, dateto)

    def return_sum_of_runs_min_period(self, datefrom: str, dateto: str):
        username = self.current_user.username
        return self._run_repository.return_run_sum_min_period(username, datefrom, dateto)
    
    def return_sum_of_runs_min_type_period(self, type: int, datefrom: str, dateto: str):
        username = self.current_user.username
        type = type
        return self._run_repository.return_run_sum_min_types_period(username, type, datefrom, dateto)

    def return_sum_of_runs_km_period(self, datefrom: str, dateto: str):
        username = self.current_user.username
        return self._run_repository.return_run_sum_km_period(username, datefrom, dateto)
    
    def return_max_hr(self):
        username = self.current_user.username
        max_hr = 220 - self._user_repository.return_age(username)
        return max_hr

    def return_easy_run_share(self):
        username = self.current_user.username
        try:
            return 100*self._run_repository.return_run_sum_min_types(username, 1)/self._run_repository.return_run_sum_min(username)
        except:
            return 0.0

    def return_easy_run_share_period(self, datefrom: str, dateto: str):
        username = self.current_user.username
        try:
            return 100*self._run_repository.return_run_sum_min_types_period(username, 1, datefrom, dateto)/self._run_repository.return_run_sum_min_period(username, username, 1, datefrom, dateto)

        except:
            return 0.0

run_calendar_service = RunCalendarService()
