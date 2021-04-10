class Credential:
    credential_list = []  # Created an empty credential list

    def __init__(self, account, password):
        """
        The init method defines the properties of the object
        :param account:
        :param password:
        """
        self.account = account
        self.password = password
