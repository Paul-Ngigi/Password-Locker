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

    def save_credential(self):
        """
        Saving the user credentials
        :return:
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        Deleting the user credentials
        :return:
        """
        Credential.credential_list.remove(self)
