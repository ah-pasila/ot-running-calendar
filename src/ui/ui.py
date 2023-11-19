from entities import Plan

class Ui:
    def __init__self(self):
        self.running_plan = Plan()

def execute(self):
    print("Add your coming run:")
    date_part = input()
    description_part = input()
    length_part = input()
    self.running_plan(date_part, description_part, length_part)    

ui = Ui()
ui.execute()
