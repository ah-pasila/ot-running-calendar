""" 
Class for creating Run calendar service
        Args: 
            user_repository: class responsible for data operations related to user
            run_repository: class responsible for data operations related to runs

ChatGPT was used to find typos and problems from the code.
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

    def __init__(
        self,
        user_repository=default_user_repository,
        run_repository=default_run_repository
    ):
        """Constructor of the class, sets up user_repository and run_repository for data operations
        creates base for logged in User information and sets default login_status = False
        """
        self._user_repository = user_repository
        self._run_repository = run_repository
        self.current_user = User("", "", "", "")
        self.login_status = False

    def add_user(self, username: str, password: str, gender: str, age: int):
        """add_user adds User object to user database using user_repository
        """
        user = User(username, password, gender, age)
        return self._user_repository.add_user(user)

    def login_user(self, given_username: str, given_password: str):
        """login_user checks that given username exists in the database and 
        validates that given password matches to username's password
        if this is the case, returns True, if not returns False
        if login is succesful, username is saved to self.current_user 
        object to be used during the "session"
        """
        if self.check_username(given_username) == True and \
                self._user_repository.check_password_correct(given_username, given_password):
            self.login_status = True
            self.current_user = User(given_username, "", "", "")
            return True
        else:
            return False

    def check_username(self, given_username):
        """check_username checks that given username exists in the database
        if this is the case, returns True, if not returns False
        """
        if self._user_repository.check_username_exists(given_username) == True:
            return True
        else:
            return False

    def logout_user(self):
        """logout_user updates user's login status as False
        user's username is deleted from the self.current_user 
        because the "session" has ended
        """
        self.login_status = False
        self.current_user = User("", "", "", "")

    def add_run(self, day: str, run_type: str, duration: str, length: int,\
                description: str, username: str):
        """add_run adds Run object to run database using run_repository
        """
        username = self.current_user.username
        run = Run(day, run_type, duration, length, description, username)
        return self._run_repository.add_run(run)

    def remove_run(self, day: str):
        """add_remove removes user's run from a given day
        """
        username = self.current_user.username
        self._run_repository.remove_run(username, day)

    def return_all_runs(self, datefrom: str, dateto: str):
        username = self.current_user.username
        return self._run_repository.return_all_runs(username, datefrom, dateto)

    def return_number_of_runs(self, datefrom: str, dateto: str):
        """return_all_runs returns all user's runs from a given period or 
        from today on
        """
        username = self.current_user.username
        return self._run_repository.return_run_count(username, datefrom, dateto)

    def return_sum_of_runs_min(self, datefrom: str, dateto: str):
        """return_number_of_runs returns number of runs from a given period or 
        from today on
        """
        username = self.current_user.username
        return self._run_repository.return_run_sum_min(username, datefrom, dateto)

    def return_sum_of_runs_min_type(self, run_type: int, datefrom: str, dateto: str):
        """return_sum_of_runs_min returns sums (in minutes) of runs from a given period 
        or from today on
        """
        username = self.current_user.username
        return self._run_repository.return_run_sum_min_types(username, run_type, datefrom, dateto)

    def return_sum_of_runs_km(self, datefrom: str, dateto: str):
        """return_sum_of_runs_km returns sums (in kilometeres) of 
        runs from a given period or from today on
        """
        username = self.current_user.username
        return self._run_repository.return_run_sum_km(username, datefrom, dateto)

    def return_max_hr(self):
        """return_max_hr returns user's maximum heartrate based on age
        """
        username = self.current_user.username
        max_hr = 220 - self._user_repository.return_age(username)
        return max_hr

    def return_easy_run_share(self, datefrom: str, dateto: str):
        """return_easy_run_share returns the share of easy runs (level 1) of users all 
        runs from a given period or from today on
        """
        username = self.current_user.username
        try:
            return 100*self._run_repository.return_run_sum_min_types(username, 1, datefrom, dateto)\
                / self._run_repository.return_run_sum_min(username, datefrom, dateto)
        except:
            return 0.0


run_calendar_service = RunCalendarService()
