# Class for runs

class Run:
    def __init__(self, day=None, description=None, length=None, username=None):
        self.day = day
        self.description = description
        self.length = length
        self.username = username

# Day: planned day for the run
# Description: description of the run (easy/moderate/hard)
# Length: planned length for the run in kilometeres
# Username: user who created the run
