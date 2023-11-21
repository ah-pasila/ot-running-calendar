from plan import Plan
from calendar import Calendar

class Ui:

    def __init__self(self, ui_view):
        self.ui_view = None

    def execute(self):
        while True:
            option = input("Plan a run - enter 1 // Print running calendar - enter 2 // Escape - enter any other key: ")
            if option == "1":
                print("Add your coming run")
                date_part = input("Set date: ")
                description_part = input("Set description of the run (easy/moderate/hard): ")
                length_part = input("Set length in km: ")
                self.running_plan.add_run(date_part, description_part, length_part)
            elif option =="2":
                self.running_plan.print_runs()
            else:
                print("Goodbye")
                break

userinterface = Ui()
userinterface.running_plan = Plan()
userinterface.execute()
