from services.run_calendar_service import Run_calendar_service
#Kysytty ChatGPT:ltä neuvoa koodin virheiden korjaamiseen -> löytyi typo luokan määrittelystä ja execute.metodista#
class Ui:

    def __init__(self):
        userinterface = Ui()
        self.run_service = Run_calendar_service()
    
    def execute(self):
        print("Welcome to the running calendar")
        userinterface.run_service.running_calendar.print_current_year_calendar()
        while True:
            option = input("Plan a run - enter 1 // Print running calendar - enter 2 // Escape - enter any other key: ")
            if option == "1":
                print("Add your coming run")
                date_part = input("Set date: ")
                description_part = input("Set description of the run (easy/moderate/hard): ")
                length_part = input("Set length in km: ")
                userinterface.run_service.add_run(date_part, description_part, length_part)
            elif option =="2":
                userinterface.run_service.print_runs()
            else:
                print("Goodbye")
                break

userinterface = Ui()
userinterface.execute()