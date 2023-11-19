#Base for running plan

class Plan:
    def __init__(self):
        self.run_plan = []

    def add_run(self, day: str, description:str, length: str):
        self.run_plan = dict(day = day, description = description, length = length)

    def print_all_exercises(self):
        print(self.run_plan)

week1 = Plan()
week1.add_run("20.11.2023", "Pk-lenkki Töölönlahti", "5")
week1.print_all_exercises()