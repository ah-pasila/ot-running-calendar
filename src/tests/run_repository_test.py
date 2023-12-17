import unittest
from entities.run import Run
from repositories.run_repository import (
    run_repository as default_run_repository
)

class TestRunRepository(unittest.TestCase):
    def setUp(self, run_repository=default_run_repository):
        self.test_run_repository = run_repository

    def test_save_run_data_into_db(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 40, 5, "...","testuser"))
        self.test_run_repository.return_run_count() == 1