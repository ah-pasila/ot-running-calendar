import unittest
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

class TestUserRepository(unittest.TestCase):
    def setUp(self, user_repository=default_user_repository):
        self.test_user_repository = user_repository
        self.test_user_repository.remove_all_users()

    def test_save_user_data_into_db(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "f", 25))
        self.test_user_repository.return_user_count() == 1