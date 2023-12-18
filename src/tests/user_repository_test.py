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
      
    def test_save_users_data_into_db(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "f", 25))
        self.test_user_repository.add_user(User("testuser1", "testpassword1", "m", 35))
        self.test_user_repository.add_user(User("testuser2", "testpassword2", "m", 45))
        self.test_user_repository.return_user_count() == 3

    def test_return_existing_username(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "f", 25))
        self.assertEqual(self.test_user_repository.check_username_exists("testuser"), True)

    def test_return_non_existing_username(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "f", 25))
        self.assertEqual(self.test_user_repository.check_username_exists("testuserX"), False)

    def test_return_age(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "f", 25))
        self.assertEqual(self.test_user_repository.return_age("testuser"), 25)
    
    def test_check_correct_password(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "f", 25))
        self.assertEqual(self.test_user_repository.check_password_correct("testuser","testpassword"), True)
    
    def test_check_not_correct_password(self):
        self.test_user_repository.add_user(User("testuser", "testpassword", "f", 25))
        self.assertEqual(self.test_user_repository.check_password_correct("testuser","testpassword222"), False)

    def test_remove_users(self):
        self.test_user_repository.add_user(User("testuser1", "testpassword", "f", 25))
        self.test_user_repository.add_user(User("testuser2", "testpassword", "f", 25))
        self.test_user_repository.remove_all_users()
        self.test_user_repository.return_user_count() == 0
      