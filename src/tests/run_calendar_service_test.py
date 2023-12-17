import unittest
from services.run_calendar_service import RunCalendarService

class TestRunRepository(unittest.TestCase):
    def setUp(self):
        self.test_run_calendar_service = RunCalendarService()

