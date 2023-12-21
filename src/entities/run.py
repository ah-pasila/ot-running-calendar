"""Class for each run to be completed

    Attributes:
        day: planned date (YYYY-MM-DD) for the run
        type: easy - 1 / moderate - 2 / hard - 3
        duration: planned duration for the run in minutes
        length: planned length for the run in kilometeres
        description: voluntary description of the run
        username: user who created the run
"""


class Run:

    def __init__(self, day: str, run_type: str, duration: int, length: int,
                 decsription: str, username: str):
        """Constructor of the class

        Args:
            day (str): date (YYYY-MM-DD) for the run
            type (str): type of run, easy - 1 / moderate - 2 / hard - 3
            duration (int): duration for the run in minutes
            length (int): length of the run in kilometers
            description (str): voluntary description of the run
            username (str): username of the logged in user who created the run
        """

        self.day = day
        self.run_type = run_type
        self.duration = duration
        self.length = length
        self.description = decsription
        self.username = username
