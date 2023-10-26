# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

import petpals.database.db_interface as db_interface


# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Load kv files
Builder.load_file('create_account_ub.kv')


# --- App Components --- #
class CreateAccountUserBackend(App):
    """
    Represents the user-side Create Account page.
    """
    def build(self):
        return CreateAccountBoxLayout()


class CreateAccountBoxLayout(Widget):
    """
    Contains the structure and functionality of the Create Account page.
    """
    def __init__(self, **kwargs):
        super(CreateAccountBoxLayout, self).__init__(**kwargs)
        self.db = db_interface.Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    email_input = ObjectProperty(None)
    password1_input = ObjectProperty(None)
    password2_input = ObjectProperty(None)
    name_input = ObjectProperty(None)

    def create_account(self):
        """
        Creates a new public Account. Successful creation if the required fields (email, password) are filled out correctly. Unsuccessful creation if any of the required fields are left blank, email is already registered, or passwords do not match.
        """
        email = self.email_input.text
        password1 = self.password1_input.text
        password2 = self.password2_input.text
        name = self.name_input.text

        # If any required fields are left blank
        if email == '' or password1 == '' or password2 == '':
            # PLACEHOLDER: error message
            print('Error: Failed to create account. Missing required field(s).')
            return
        # If email is already registered
        accounts = self.find_account(email)
        if len(accounts) > 0:
            # PLACEHOLDER: error message
            print('Error: Failed to create account. Email is already registered to an account.')
            return
        # If passwords do not match
        if password1 != password2:
            # PLACEHOLDER: error message
            print('Error: Failed to create account. Passwords do not match.')
            return

        # Create account
        self.add_account(email, password1, name)
        # PLACEHOLDER: success message
        print('Successful account creation!')

    def find_account(self, email):
        """
        Returns a list containing the id_account for the Account with the matching email. Returns an empty list if no such Account exists. There should not be multiple Accounts with the same email.

        :param str email: target email
        :return: [(id_account,)]
        """
        selectID_cmd = "SELECT id_account FROM Accounts WHERE email = %s"
        selectID_params = (email,)
        selectID_result = self.db.query(selectID_cmd, selectID_params)
        return selectID_result

    def add_account(self, email, password, name):
        """
        Adds a new public Account to the database with the given values for its attributes.

        :param str email: email of the new Account
        :param str password: password of the new Account
        :param str name: name associated with the new Account
        :return: None
        """
        addAccount_cmd = "INSERT INTO Accounts (email, password, name) VALUES (%s, %s, %s)"
        addAccount_params = (email, password, name)
        self.db.query(addAccount_cmd, addAccount_params)


# --- Main Method --- #
if __name__ == "__main__":
    CreateAccountUserBackend().run()
