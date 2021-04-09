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

    def test_init(self):
        """
        test_init test case tests if the objects are being initiated correctly
        :return:
        """
        self.assertEqual(self.new_user.firstName, "Paul")
        self.assertEqual(self.new_user.lastName, "Ngigi")
        self.assertEqual(self.new_user.password, "secure2342")
        self.assertEqual(self.new_user.phoneNumber, "0714060467")
        self.assertEqual(self.new_user.email, "paulkush7777@gmail.com")


if __name__ == '__main__':
    unittest.main()
