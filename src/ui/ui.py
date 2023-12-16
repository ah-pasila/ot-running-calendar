""" In this class, ChatGPT was used to find problems in code structures and debugging
""" 

import calendar
from datetime import date
from services.run_calendar_service import Run_calendar_service


class UI:
    """Class responsible for creating the ui of the service and starting the service
    """
    def __init__(self):
        self.run_calendar = Run_calendar_service()

    def log_user_in(self):
        print("Welcome to the running calendar!")
        while True:
            option = input(
                "Login to the running calendar - enter 1 // Add new user - enter 2 // Escape - enter any other key: ")
            if option == "1":
                print("Enter username and password to login")
                given_username = input("Enter username: ")
                given_password = input("Enter password: ")
                while True:
                    if self.run_calendar.login_user(given_username, given_password) == True:
                        print("Welcome to the running calendar!")
                        self.add_plan()
                        break
                    else:
                        print("Username or password was incorrect")
                        option = input("Try again - enter 1 // Escape - enter any other key: ")
                        if option == "1":
                            self.log_user_in()
                            break
                        else:                
                            print("Goodbye")
                            break
                break
            elif option == "2":
                self.add_user_info()
                continue
            else:
                print("Goodbye")
                break

    def add_user_info(self):
        print("Welcome to add user info")
        username = input("Set username: ")
        password = input("Set password (length min 8 character): ")
        gender = input("Gender (F-M-Other): ")
        age = input("Age (in years): ")
        self.run_calendar.add_user(username, password, gender, age)

    def add_plan(self):
        print("It's time to plan your runs for the coming months:\n")
        today = date.today()
        current_year = today.year
        current_month = today.month
        print(calendar.month(current_year, current_month))
        if current_month == 12:
            year = current_year + 1
            month = 1
            print(calendar.month(year, month))
        else:
            year = current_year
            next_month = month + 1
            print(calendar.month(year, next_month))
        while True:
            option = input(
                "Plan a run - enter 1 // Print running calendar - enter 2 // Escape - enter any other key: ")
            if option == "1":
                print("Add your coming run")
                date_part = input("Set date: ")
                description_part = input(
                    "Set description of the run (easy/moderate/hard): ")
                length_part = input("Set length in km: ")
                self.run_calendar.add_run(
                    date_part, description_part, length_part, "")
            elif option == "2":
                self.run_calendar.print_runs()
            else:
                self.run_calendar.logout_user()
                print("Goodbye")
                break
