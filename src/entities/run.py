class Run:

    """Class for each run to be completed

    Attributes:
        day: planned day for the run
        description: description of the run (easy/moderate/hard)
        length: planned length for the run in kilometeres
        username: user who created the run

    """
   
    def __init__(self, day=None, description=None, length=None, username=None):
        self.day = day
        self.description = description
        self.length = length
        self.username = username