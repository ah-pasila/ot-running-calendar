# Käyttöliittymä
# Kysytty ChatGPT:ltä neuvoa koodin rakenteen ja virheiden korjaamiseen -> löytyi mm. typo luokan määrittelystä ja execute.metodista

import calendar
from datetime import date
from services.run_calendar_service import Run_calendar_service


class UI:

    def __init__(self):
        self.run_calendar = Run_calendar_service()

    def add_user_info(self):
        print("Welcome to add user info")
        username = input("Set username: ")
        password = input("Set password (length min 8 character): ")
        gender = input("Gender (F-M-Other): ")
        age = input("Age (in years): ")
        self.run_calendar.add_user(username, password, gender, age)

    def add_plan(self):
        print("Welcome to the running calendar!")
        print("It's time to plan your runs for the coming months:\n")
        today = date.today()
        current_year = today.year
        current_month = today.month
        print(calendar.month(current_year, current_month))
        if current_month == 12:
            year = current_year + 1
            month = 1
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
                    date_part, description_part, length_part)
            elif option == "2":
                self.run_calendar.print_runs()
            else:
                print("Goodbye")
                break