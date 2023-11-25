# User information, basic information for authorization
# Additional & voluntary personal information

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_gender(self, gender):
        self.gender = gender

    def add_age(self, age):
        self.age = age