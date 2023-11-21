from plan import Plan

class Ui:

    def __init__self(self):
        self.running_plan = Plan()

    def execute(self):
        while True:
            print("Add your coming run: ")
            date_part = input("Set date: ")
            description_part = input("Set description of the run: ")
            length_part = input("Set length in km: ")
            self.running_plan(date_part, description_part, length_part)

userinterface = Ui()
userinterface.execute()
