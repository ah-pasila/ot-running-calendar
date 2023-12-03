#Base for running plan containing future runs

class Plan:
    def __init__(self):
        self.run_plan = []

    def add_run(self, day: str, description:str, length: str):
        self.run_plan.append(dict(day = day, description = description, length = length))

    def print_runs(self):
        print(self.run_plan)