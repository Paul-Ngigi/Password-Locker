from user import User
from credentials import Credential


def create_user(username, password, email):
    """
    Function to create a new user
    :param username:
    :param password:
    :param email:
    :return:
    """
    new_user = User(username, password, email)
    return new_user


def save_user(user):
    """
    Function to save our user
    :param user:
    :return:
    """
    User.save_user(user)


def delete_user(user):
    """
    Function to delete a user
    :param user:
    :return:
    """
    User.delete_user(user)
