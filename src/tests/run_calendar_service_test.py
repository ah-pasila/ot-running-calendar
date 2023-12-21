import unittest
from entities.user import User
from services.run_calendar_service import RunCalendarService
from repositories.user_repository import (
    UserRepository as default_user_repository
)

from repositories.run_repository import (
    RunRepository as default_run_repository
)


class TestRunCalendarService(unittest.TestCase):
    def setUp(self):
        self.test_run_calendar_service = RunCalendarService()
        self.test_user_repository = default_user_repository
        self.test_run_repository = default_run_repository
        self.test_user_repository.remove_all_users()
        self.test_user_repository.add_user(
            User("testikayttaja", "testisala", "f", 40))

    def test_check_login_status(self):
        self.test_run_calendar_service.login_status == False

    def test_return_login_status(self):
        self.test_run_calendar_service.login_user("testikayttaja", "testisala")
        self.assertEqual(self.test_run_calendar_service.login_status, True)

