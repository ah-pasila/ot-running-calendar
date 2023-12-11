import unittest
from entities.run import Run
from services.run_calendar_service import run_calendar_service

class TestRun(unittest.TestCase):
    def setUp(self):
        self.run_calendar_service = Run()

    def test_adding_run(self):
        self.run.add_run("20.11.2023", "easy", "5")
        self.assertEqual(self.run.print_all_exercises(
        ), "{'day': '20.11.2023', 'description': 'easy', 'length': '5'}")
