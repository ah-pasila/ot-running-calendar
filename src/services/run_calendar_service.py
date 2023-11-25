from entities.plan import Plan
from entities.user import User

class Run_calendar_service:

    def __init__self(self):
        self.user = User("test1", "test2")
        self.running_plan = Plan()

# Testing code 

palvelu = Run_calendar_service()
palvelu.add_run("1", "2", "3")

