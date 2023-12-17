import unittest
from entities.run import Run
from repositories.run_repository import (
    run_repository as default_run_repository
)

class TestRunRepository(unittest.TestCase):
    def setUp(self, run_repository=default_run_repository):
        self.test_run_repository = run_repository
        self.test_run_repository.remove_all_runs()

    def test_save_run_data_into_db(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 40, 5, "...","testuser"))
        self.test_run_repository.return_run_count("testuser") == 1

    def test_remove_run_works(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 40, 5, "...","testuser"))
        self.test_run_repository.add_run(Run("2024-01-05", "2", 40, 5, "...","testuser"))
        self.test_run_repository.remove_run("2024-01-05")
        self.test_run_repository.return_run_count("testuser") == 1

    def test_get_users_run(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 40, 5, "...","testuser1"))
        self.test_run_repository.add_run(Run("2024-01-02", "1", 40, 5, "...","testuser2"))
        self.test_run_repository.return_run_count("testuser1") == 1

    def test_min_sum_is_correct(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 100, 5, "...","testuser1"))
        self.test_run_repository.add_run(Run("2024-01-02", "1", 40, 5, "...","testuser1"))
        self.assertEqual(self.test_run_repository.return_run_sum_min("testuser1"), 140)

    def test_km_sum_is_correct(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 100, 5, "...","testuser1"))
        self.test_run_repository.add_run(Run("2024-01-02", "1", 40, 5, "...","testuser1"))
        self.assertEqual(self.test_run_repository.return_run_sum_km("testuser1"), 10)

    def test_min_sum_is_correct_period(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 100, 5, "...","testuser1"))
        self.test_run_repository.add_run(Run("2024-01-02", "1", 40, 5, "...","testuser1"))
        self.test_run_repository.add_run(Run("2024-01-05", "1", 40, 5, "...","testuser1"))
        self.assertEqual(self.test_run_repository.return_run_sum_min_period("testuser1", '2024-01-02', '2024-01-05'), 80)

    def test_km_sum_is_correct_period(self):
        self.test_run_repository.add_run(Run("2024-01-01", "1", 100, 5, "...","testuser1"))
        self.test_run_repository.add_run(Run("2024-01-02", "1", 40, 5, "...","testuser1"))
        self.test_run_repository.add_run(Run("2024-01-05", "1", 40, 5, "...","testuser1"))
        self.assertEqual(self.test_run_repository.return_run_sum_km_period("testuser1", '2024-01-02', '2024-01-05'), 10)