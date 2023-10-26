"""
Contains all functions that perform CRUD operations on the Accounts entity.
"""

def find_account(email, db):
        """
        Returns a list containing the id_account for the Account with the matching email. Returns an empty list if no such Account exists. There should not be multiple Accounts with the same email.

        :param str email: target email
        :param Database db: database to be queried
        :return: [(id_account,)]
        """
        selectID_cmd = "SELECT id_account FROM Accounts WHERE email = %s"
        selectID_params = (email,)
        selectID_result = db.query(selectID_cmd, selectID_params)
        return selectID_result

def verify_password(id_account, password, db):
        """
        Returns True if the given password matches the stored password for the Account. Returns False otherwise.

        :param int id_account: ID of the Account
        :param str password: target password
        :param Database db: database to be queried
        :return: True if the passwords match, False otherwise
        """
        selectPassword_cmd = "SELECT password FROM Accounts WHERE id_account = %s"
        selectPassword_params = (id_account,)
        selectPassword_result = db.query(selectPassword_cmd, selectPassword_params)
        stored_password = selectPassword_result[0][0]
        return password == stored_password

def is_admin(id_account, db):
        """
        Checks the credentials of the Account. Returns True if the Account is a administrative account, False otherwise (public account). id_credential equals 1 for a public account, 2 for an administrative account.

        :param int id_account: ID of the Account
        :param Database db: database to be queried
        :return: True if the Account is an administrative account, False otherwise
        """
        selectCredentials_cmd = "SELECT id_credential FROM Accounts WHERE id_account = %s"
        selectCredentials_params = (id_account,)
        selectCredentials_result = db.query(selectCredentials_cmd, selectCredentials_params)
        credentials = selectCredentials_result[0][0]
        return credentials == 2
