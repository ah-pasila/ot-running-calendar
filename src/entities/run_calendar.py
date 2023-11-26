# Base for calendar

from calendar import calendar
from datetime import date
#Pyydetty ChatGPT:ltä neuvoja luokan toimintaan, siivottu käyttämätön konstruktori
class Run_calendar:
    
    def print_current_year_calendar(self):
        today = date.today()
        year = today.year
        print(calendar(year))

    def print_next_year_calendar(self):
        today = date.today()
        year = today.year + 1
        print(calendar(year))