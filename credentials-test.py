import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the Credential contact class behaviours
    """

    def setUp(self) -> None:
        """
        Set up method to be run before each test cases
        :return:
        """
        self.new_credentials = Credential("twitter", "tweet32323")
