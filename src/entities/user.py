# User information, basic information for authorization
# Additional & voluntary personal information

class User:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def add_gender(self, gender: str):
        self.gender = gender

    def add_age(self, age):
        self.age = age

    def print_basic_info(self):
        print("User info:", self.username, self.gender, self.age)