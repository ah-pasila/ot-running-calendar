from entities.plan import Plan
from entities.user import User

class Running_calendar:

    def __init__self(self):
        self.user = None
        self.user = User()
        self.running_plan = Plan()
    
    def add_run(self, date_part, description, run_length):
        self.running_plan.add_run(date_part, description, run_length)

## Käyttäjän lisäämiseen liittyvät tehtävät