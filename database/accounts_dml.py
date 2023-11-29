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

def add_account(email, password, name, db):
        """
        Adds a new public Account to the database with the given values for its attributes.

        :param str email: email of the new Account
        :param str password: password of the new Account
        :param str name: name associated with the new Account
        :param Database db: database to be queried
        :return: None
        """
        addAccount_cmd = "INSERT INTO Accounts (email, password, name) VALUES (%s, %s, %s)"
        addAccount_params = (email, password, name)
        db.query(addAccount_cmd, addAccount_params)

def update_account_name(id_account, name, db):
        """
        Updates the Account's name with the given value.

        :param int id_account: ID of the Account
        :param str name: new name
        :param Database db: database to be queried
        :return: None
        """
        updateAccountName_cmd = "UPDATE Accounts SET name = %s WHERE id_account = %s"
        updateAccountName_params = (name, id_account)
        db.query(updateAccountName_cmd, updateAccountName_params)

def update_account_email(id_account, email, db):
        """
        Updates the Account's name with the given value.

        :param int id_account: ID of the Account
        :param str email: new email
        :param Database db: database to be queried
        :return: None
        """
        updateAccountEmail_cmd = "UPDATE Accounts SET email = %s WHERE id_account = %s"
        updateAccountEmail_params = (email, id_account)
        db.query(updateAccountEmail_cmd, updateAccountEmail_params)

def update_account_password(id_account, password, db):
        """
        Updates the Account's password with the given value.

        :param int id_account: ID of the Account
        :param str password: new password
        :param Database db: database to be queried
        :return: None
        """
        updateAccountPassword_cmd = "UPDATE Accounts SET password = %s WHERE id_account = %s"
        updateAccountPassword_params = (password, id_account)
        db.query(updateAccountPassword_cmd, updateAccountPassword_params)

def delete_account(id_account, db):
        """
        Deletes the Account.

        :param int id_account: ID of the Account
        :param Database db: database to be queried
        :return: None
        """
        deleteAccount_cmd = "DELETE FROM Accounts WHERE id_account = %s"
        deleteAccount_params = (id_account,)
        db.query(deleteAccount_cmd, deleteAccount_params)


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

def add_liked_animal(id_account, id_animal, db):
        """
        Adds a Liked_Animal entry to the database with the given attribute values.

        :param int id_account: ID of the specified Account
        :param int id_animal: ID of the specified Animal
        :param Database db: database to be queried
        :return: None
        """
        addLikedAnimal_cmd = "INSERT INTO Liked_Animals (id_account, id_animal) VALUES (%s, %s)"
        addLikedAnimal_params = (id_account, id_animal)
        db.query(addLikedAnimal_cmd, addLikedAnimal_params)

def remove_liked_animal(id_account, id_animal, db):
        """
        Removes a Liked_Animal entry from the databse with the given attributes values.

        :param int id_account: ID of the specified Account
        :param int id_animal: ID of the specified Animal
        :param Database db: database to be queried
        :return: None
        """
        removeLikedAnimal_cmd = "DELETE FROM Liked_Animals WHERE id_account = %s AND id_animal = %s"
        removeLikedAnimal_params = (id_account, id_animal)
        db.query(removeLikedAnimal_cmd, removeLikedAnimal_params)

def get_liked_animals(id_account, db):
        """
        Returns the list of Liked Animals for the Account with the specified ID.

        :param int id_account: ID of the target Account
        :param Database db: database to be queried
        :return: [(id_animal)]
        """
        getLikedAnimals_cmd = "SELECT id_animal FROM Liked_Animals WHERE id_account = %s"
        getLikedAnimals_params = (id_account,)
        getLikedAnimals_result = db.query(getLikedAnimals_cmd, getLikedAnimals_params)
        return getLikedAnimals_result
