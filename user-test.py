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
        self.new_user = User("Paul", "Ngigi", "0714060467", "paulkush7777@gmail.com")  # create contact object

    def test_init(self):
        """
        test_init test case tests if the objects are being initiated correctly
        :return:
        """
        self.assertEqual(self.new_user.firstName, "Paul")
        self.assertEqual(self.new_user.lastName, "Ngigi")
        self.assertEqual(self.new_user.phoneNumber, "0714060467")
        self.assertEqual(self.new_user.email, "paulkush7777@gmail.com")

    def test_save_user(self):
        """
        test_save_user test case tests if a user is being save correctly
        in the user list
        :return:
        """
        self.new_user.save_user()

        self.assertEqual(len(User.user_list), 1)

    def tearDown(self) -> None:
        User.user_list = []

    def test_save_multiple_users(self):
        """
        test_save_multiple_users test case tests if multiple users can be saved correctly
        in the user list
        :return:
        """
        self.new_user.save_user()
        test_user = User("test", "user", "0711111111", "test@user.com")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        """
        test_delete_user test case tests if a user can be deleted successfully from the
        user list
        :return:
        """
        self.new_user.save_user()
        test_user = User("test", "user", "0711111111", "test@user.com")
        test_user.save_user()

        test_user.delete_user()

        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
