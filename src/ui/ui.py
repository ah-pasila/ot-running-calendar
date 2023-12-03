#Käyttöliittymä
#Kysytty ChatGPT:ltä neuvoa koodin rakenteen ja virheiden korjaamiseen -> löytyi mm. typo luokan määrittelystä ja execute.metodista

from services.run_calendar_service import Run_calendar_service

class UI:

    def __init__(self):
        self.run_calender = Run_calendar_service()

    def execute(self):
        print("Welcome to the running calendar")
        self.run_calender.print_calendar()
        while True:
            option = input("Plan a run - enter 1 // Print running calendar - enter 2 // Escape - enter any other key: ")
            if option == "1":
                print("Add your coming run")
                date_part = input("Set date: ")
                description_part = input("Set description of the run (easy/moderate/hard): ")
                length_part = input("Set length in km: ")
                self.run_calender.add_run(date_part, description_part, length_part)
            elif option =="2":
                self.run_calender.print_runs()
            else:
                print("Goodbye")
                break