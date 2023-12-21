import unittest
from entities.user import User
from services.run_calendar_service import RunCalendarService
from repositories.user_repository import (
    user_repository as default_user_repository
)

from repositories.run_repository import (
    run_repository as default_run_repository
)


class TestRunCalendarService(unittest.TestCase):
    def setUp(self):
        self.test_run_calendar_service = RunCalendarService()
        self.test_user_repository = default_user_repository
        self.test_run_repository = default_run_repository
        self.test_user_repository.remove_all_users()
        self.test_run_repository.remove_all_runs()

    def test_check_login_status(self):
        self.test_user_repository.add_user(User("testikayttaja", "testisala", "f", 40))
        self.test_run_calendar_service.login_status == False

    def test_return_login_status(self):
        self.test_user_repository.add_user(User("testikayttaja", "testisala", "f", 40))
        self.test_run_calendar_service.login_user("testikayttaja", "testisala")
        self.assertEqual(self.test_run_calendar_service.login_status, True)
 
    def test_run_saving_into_db(self):
        self.test_run_calendar_service.add_run("2023-12-20","3",30,6,"","testikayttaja")
        self.test_run_repository.return_run_count_in_db() == 1

    def test_run_delete_from_db(self):
        self.test_run_calendar_service.add_run("2023-12-20","3",30,6,"","testikayttaja")
        self.test_run_calendar_service.remove_run("2023-12-20")
        self.test_run_repository.return_run_count_in_db() == 0

    def test_user_saving_into_db(self):
        self.test_run_calendar_service.add_user("testikayttaja2","testisala","f","18")
        self.test_user_repository.return_user_count() == 1

    def test_check_existing_username(self):
        self.test_run_calendar_service.add_user("testikayttaja2","testisala","f","18")
        self.test_run_calendar_service.check_username("testikayttaja2") == True
        
    def test_check_not_existing_username(self):
        self.test_run_calendar_service.add_user("testikayttaja3","testisala","f","18")
        self.test_run_calendar_service.check_username("testikayttaja2") == True