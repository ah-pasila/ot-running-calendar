class Run:

    """Class for each run to be completed

    Attributes:
        day: planned day for the run
        type: easy - 1 / moderate - 2 / hard - 3
        length: planned length for the run in kilometeres
        description: voluntary description of the run
        username: user who created the run

    """
   
    def __init__(self, day=None, type=None, duration=None, length=None, decsription=None, username=None):
        self.day = day
        self.type = type
        self.duration = duration
        self.length = length
        self.description = decsription
        self.username = username