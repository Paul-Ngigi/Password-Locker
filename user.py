class User:
    user_list = []  # Created an empty user list

    def __init__(self, username, password, email):
        """
        The __init__ method defines properties of the object
         :param username:
        :param password:
        :param email:
        """
        self.username = username
        self.password = password
        self.email = email

    def save_user(self):
        """
        Method to add a new user to the user list
        :return:
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        Method to delete user from the contact list
        :return:
        """
        User.user_list.remove(self)
