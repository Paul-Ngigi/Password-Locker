import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the User contact class behaviours
    """

    def setUp(self) -> None:
        """
        Set up method to run before each test cases.
        :return:
        """
        self.new_user = User("Paul", "Ngigi", "secure2342", "0714060467",
                             "paulkush7777@gmail.com")  # create contact object

