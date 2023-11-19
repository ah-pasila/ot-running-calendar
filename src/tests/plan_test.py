import unittest
from entities.plan import Plan

class Test_plan(unittest.TestCase):
    def setUp(self):
        self.week = Plan()

    def test_adding_run(self):
        self.week.add_run("20.11.2023","Pk-lenkki Töölönlahti","5")
        self.assertEqual(self.week.print_all_exercises(), "{'day': '20.11.2023', 'description': 'Pk-lenkki Töölönlahti', 'length': '5'}")