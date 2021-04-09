class User:
    user_list = []  # Created an empty user list

    def __init__(self, first_name, last_name, password, phone_number, email):
        """
        The __init__ method defines properties of the object
        :param first_name:
        :param last_name:
        :param password:
        :param phone_number:
        :param email:
        """
        self.firstName = first_name
        self.lastName = last_name
        self.password = password
        self.phoneNumber = phone_number
        self.email = email
