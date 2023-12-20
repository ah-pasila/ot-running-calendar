"""Class responsible for creating the ui of the service and starting the service

In this class, ChatGPT was used to find problems in code structures and debugging
"""

import calendar
import datetime
from datetime import date
from services.run_calendar_service import RunCalendarService


class UI:

    def __init__(self):
        self.run_calendar = RunCalendarService()

    def execute_app(self):
        print("Welcome to the running calendar!")
        while True:
            _option = input(
                "Login to the running calendar - enter 1 // Add new user - enter 2 // Escape - enter any other key: ")
            if _option == "1":
                self._start_user_login()
                break
            elif _option == "2":
                self._add_user_info()
                continue
            else:
                print("Goodbye")
                break

    def _start_user_login(self):
        print("Enter username and password to login")
        given_username = input("Enter username: ")
        given_password = input("Enter password: ")
        while True:
            if self.run_calendar.login_user(given_username, given_password) == True:
                print("Welcome to the running calendar!")
                self._add_plan()
                break
            else:
                print("Username or password was incorrect")
                option = input(
                    "Try again - enter 1 // Escape - enter any other key: ")
                if option == "1":
                    self.execute_app()
                    break
                else:
                    print("Goodbye")
                    break

    def _add_user_info(self):
        print("Welcome to add user info")
        while True:
            username = str(input("Set username: "))
            if self.run_calendar.check_username(username) == False:
                break
            else:
                print("Username already taken, choose another one")
        while True:
            password = str(input("Set password (length min 8 character): "))
            if len(password) >= 8:
                break
            else:
                print("Password must be at least 8 characters long")
        while True:
            try:
                gender = str(input("Gender (f-m-other): "))
                if gender in ("f", "m", "other"):
                    break
                else:
                    print("Gender must be f, m or other")
            except ValueError:
                print("Gender must be f, m or other")
        while True:
            try:
                age = int(input("Age (in full years): "))
                if age >= 0 and age <= 120:
                    break
                else:
                    print("Enter age between 0-120 years")
            except ValueError:
                print("Enter age between 0-120 years in numbers")
        self.run_calendar.add_user(username, password, gender, age)

        """add_user_info saves user info into database
            ChatGPT was used to help correct age validation check problems
        """

    def _add_plan(self):
        print("It's time to plan your runs for the coming months:\n")
        _today = date.today()
        _current_year = _today.year
        _current_month = _today.month
        print(calendar.month(_current_year, _current_month))
        if _current_month == 12:
            _year = _current_year + 1
            _month = 1
            print(calendar.month(_year, _month))
        else:
            _year = _current_year
            _next_month = _month + 1
            print(calendar.month(_year, _next_month))
        while True:
            _option = input(
                "Plan a run - enter 1 // Print running calendar - enter 2 // Print statistics - enter 3 // Remove run - enter 4 // Escape - enter any other key: ")
            if _option == "1":
                self._add_run()
            elif _option == "2":
                self._show_runs()
            elif _option == "3":
                self._show_statistics()
            elif _option == "4":
                while True:
                    try:
                        removedate = str(
                            input("Enter date from which plan is removed (YYYY-MM-DD): "))
                        if datetime.date.fromisoformat(removedate):
                            break
                        else:
                            print(
                                "Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
                    except ValueError:
                        print(
                            "Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
                self.run_calendar.remove_run(removedate)
            else:
                self.run_calendar.logout_user()
                print("Goodbye")
                break

    def _add_run(self):
        print("Add your coming run")
        while True:
            try:
                date_part = str(input("Enter date (YYYY-MM-DD): "))
                if datetime.date.fromisoformat(date_part):
                    break
                else:
                    print("Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
            except ValueError:
                print("Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")

        print("Define the intensity of the run\n1 - easy 60-70% / maximum heartrate, your max: ",
              self.run_calendar.return_max_hr(), "\n2 - moderate 70-85%\n3 - hard 85-100 %")

        while True:
            type_part = str(input("Enter run type 1, 2 or 3: "))
            if type_part in ("1", "2", "3"):
                break
            else:
                print("Type must be 1, 2 or 3")
        while True:
            try:
                duration_part = int(
                    input("Enter duration of the run in minutes: "))
                if duration_part >= 1 and duration_part <= 3000:
                    break
                else:
                    print("Enter duration between 1-3000 minutes")
            except ValueError:
                print("Enter duration between 1-3000 minutes")
        while True:
            try:
                length_part = int(
                    input("Enter expected length in kilometers: "))
                if (length_part >= 1 and length_part <= 200):
                    break
                else:
                    print("Enter length between 0-200 kilometers")
            except ValueError:
                print("Enter length between 0-200 kilometers")
        description_part = str(
            input("Enter description of the run (voluntary): "))
        self.run_calendar.add_run(date_part, type_part, duration_part,
                                  length_part, description_part, "")

    def _show_runs(self):
        _option = input(
            "Show all future runs - enter 1 // Select time period - enter 2 // Escape - enter any other key: ")
        if _option == "1":
            print("All future runs: ")
            print(self.run_calendar.return_all_runs("", ""))
        elif _option == "2":
            while True:
                try:
                    datefrom = str(input("Enter starting date (YYYY-MM-DD): "))
                    if datetime.date.fromisoformat(datefrom):
                        break
                    else:
                        print(
                            "Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
                except ValueError:
                    print("Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
            while True:
                try:
                    dateto = str(input("Enter end date (YYYY-MM-DD): "))
                    if datetime.date.fromisoformat(dateto):
                        break
                    else:
                        print(
                            "Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
                except ValueError:
                    print("Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
            print(self.run_calendar.return_all_runs(datefrom, dateto))
        else:
            pass

    def _show_statistics(self):
        print("************** Running plan statistics **************")
        _option = input(
            "Show statistics on all future runs - enter 1 // Select time period - enter 2 // Escape - enter any other key: ")
        if _option == "1":
            print("Number of planned runs: ",
                  (self.run_calendar.return_number_of_runs("", "")))
            print("Sum of planned runs (in minutes): ",
                  self.run_calendar.return_sum_of_runs_min("", ""))
            print("Sum of planned runs (in kms): ",
                  self.run_calendar.return_sum_of_runs_km("", ""))
            _share = self.run_calendar.return_easy_run_share("", "")
            print(
                f"Most of the running should be easy (type 1 runs),\
                    share of easy running minutes in your plan, %: {_share: .1f}")
        elif _option == "2":
            while True:
                try:
                    datefrom = str(input("Enter starting date (YYYY-MM-DD): "))
                    if datetime.date.fromisoformat(datefrom):
                        break
                    else:
                        print(
                            "Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
                except ValueError:
                    print("Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
            while True:
                try:
                    dateto = str(input("Enter end date (YYYY-MM-DD): "))
                    if datetime.date.fromisoformat(dateto):
                        break
                    else:
                        print(
                            "Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")
                except ValueError:
                    print("Enter date in correct format YYYY-MM-DD, e.g. 2024-01-30")

            print("Number of planned runs: ",
                  (self.run_calendar.return_number_of_runs(datefrom, dateto)))
            print("Sum of planned runs (in minutes): ",
                  self.run_calendar.return_sum_of_runs_min(datefrom, dateto))
            print("Sum of planned runs (in kms): ",
                  self.run_calendar.return_sum_of_runs_km(datefrom, dateto))
            _share = self.run_calendar.return_easy_run_share(datefrom, dateto)
            print(
                f"Most of the running should be easy (type 1 runs),\nshare of easy running minutes in your plan, %: {_share: .1f}")
        else:
            pass
