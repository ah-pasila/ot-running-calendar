# Base for calendar
# Pyydetty ChatGPT:ltä neuvoja luokan toimintaan

import calendar
from datetime import date


class Run_calendar:

    def __init__(self):
        pass

    def print_current_month_calendar(self):
        today = date.today()
        current_year = today.year
        current_month = today.month
        print(calendar.month(current_year, current_month))

    def print_next_month_calendar(self):
        today = date.today()
        year = today.year
        month = today.month
        if month == 12:
            year = year + 1
            month = 1
        else:
            year == year
            month = month + 1
        print(calendar.month(year, month))
