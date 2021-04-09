class User:
    user_list = []  # Created an empty user list

    def __init__(self, first_name, last_name, phone_number, email):
        """
        The __init__ method defines properties of the object
        :param first_name:
        :param last_name:
        :param phone_number:
        :param email:
        """
        self.firstName = first_name
        self.lastName = last_name
        self.phoneNumber = phone_number
        self.email = email

    def save_user(self):
        """
        Method to add a new user to the user list
        :return:
        """
        User.user_list.append(self)


