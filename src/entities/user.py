
class User:
    """_Class for users of the application.

    Attributes:
        username: username created by the user
        password: password created by the user
        gender: gender of the user
        age: age of the user
    """

    def __init__(self, username: str, password: str, gender: str, age: int):
        """Constructor of the class

        Args:
            username (str): username created by the user
            password (str): password created by the user
            gender (str): gender of the user
            age (int): age of the user
        """

        self.username = username
        self.password = password
        self.gender = gender
        self.age = age