import unittest
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

class TestUserRepository(unittest.TestCase):
    def setUp(self, user_repository=default_user_repository):
        self.test_user_repository = user_repository

    def test_adding_one_user(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "F","25"))
        self.test_user_repository.return_user_count() == 1
        