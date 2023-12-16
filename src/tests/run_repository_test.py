import unittest
from entities.run import Run
from repositories.run_repository import (
    run_repository as default_run_repository
)

class TestRunRepository(unittest.TestCase):
    def setUp(self, run_repository=default_run_repository):
        self.test_run_repository = run_repository

    def test_adding_one_run(self):
        self.test_run_repository.add_run(Run("1.1.2024", "", "1", "5"))
        self.test_run_repository.return_run_count() == 1