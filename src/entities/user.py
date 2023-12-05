# User information, basic information for authorization
# Additional & voluntary personal information

class User:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.gender = None
        self.age = None

    def add_username(self, username: str):
        self.username = username

    def add_password(self, password: str):
        self.password = password

    def add_gender(self, gender: str):
        self.gender = gender

    def add_age(self, age: str):
        self.age = age
