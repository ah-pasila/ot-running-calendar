class Run:

    """Class for each run to be completed

    Attributes:
        day: planned day for the run
        type: easy - 1 / moderate - 2 / hard - 3
        duration: planned duration for the run in full minutes
        length: planned length for the run in full kilometeres
        description: voluntary description of the run
        username: user who created the run

    """
   
    def __init__(self, day: str, type: str, duration: int, length: int, decsription: str, username: str):
        self.day = day
        self.type = type
        self.duration = duration
        self.length = length
        self.description = decsription
        self.username = username