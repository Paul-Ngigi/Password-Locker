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


def check_existing_user(username, password):
    """
    Function to check if a user exists and returns user details
    :param username:
    :param password:
    :return:
    """
    user_verification = User.user_exists(username, password)


def create_user_details(account, password):
    """
    Function to create user details
    :param account:
    :param password:
    :return:
    """
    new_user_details = Credential(account, password)
    return new_user_details


def save_user_details(details):
    """
    Function to save the user details
    :param details:
    :return:
    """
    return Credential.save_credential(details)


def display_user_details(username):
    """
    Function to display the user details
    :param username:
    :return:
    """
    return Credential.display_credentials()


def automatic_generated_password():
    """
    Function that generates an automatic password for users
    :return:
    """
    generate_password = Credential.automatic_generated_password()
    return generate_password


def main():
    print("WELCOME TO PASSWORD LOCKER")
    print("\n")
    print("Select an option: \n 1-Create an account \n 2-Login to your account \n 3-Exit Python Password Locker")
    print("\n")

    choice = int(input())

    while True:
        if choice == 1:
            print("*" * 20)
            print("Create an account")
            print("*" * 20)

            print("Enter your username")
            user_name = input()
            print("-" * 10)

            print("Enter your email")
            email = input()
            print("-" * 10)

            print("Enter a new password")
            password = input()
            print("-" * 10)

            save_user(create_user(user_name, password, email))
            print("-" * 10)

            print(f"{user_name}, you have successfully created an account. You may now login")


if __name__ == '__main__':
    main()
