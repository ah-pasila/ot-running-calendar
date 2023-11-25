# Base for calendar

from calendar import calendar
from datetime import date

class Run_calendar:
    
    def __init__(self):
        None

    def print_current_year_calendar(self):
        today = date.today()
        year = today.year
        print(calendar(year))

    def print_next_year_calendar(self):
        today = date.today()
        year = today.year + 1
        print(calendar(year))