# Base for calendar

from calendar import calendar
from datetime import date
#Pyydetty ChatGPT:ltä neuvoja luokan toimintaan
class Run_calendar:

    def __init__(self):
        pass
        
    def print_current_year_calendar(self):
        today = date.today()
        year = today.year
        print(calendar(year))
