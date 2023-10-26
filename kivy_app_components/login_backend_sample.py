# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from database.db_interface import Database


# --- Set Up --- #

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Load kv files
Builder.load_file('../kv_design_language/login_backend_sample.kv')


# --- App Components --- #
class LoginBackend(App):
    """
    Represents the Login page.
    """
    def build(self):
        return LoginBoxLayout()


class LoginBoxLayout(Widget):
    """
    Contains the structure and functionality of the Login page.
    """
    def __init__(self, **kwargs):
        super(LoginBoxLayout, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)

    def login(self):
        """
        Validates login info. Successful login if the email and password match those of an Account. Unsuccessful login if the email is not registered or password is incorrect.
        """
        email = self.email_input.text
        password = self.password_input.text

        # If email is not registered
        accounts = self.find_account(email)
        if len(accounts) == 0:
            # PLACEHOLDER: error message
            print('Error: Failed to login. Email is not registered to an account.')
            return
        # If password is incorrect
        id_account = accounts[0][0]
        if not self.verify_password(id_account, password):
            # PLACEHOLDER: error message
            print('Error: Failed to login. Password is incorrect.')
            return

        # Successful login
        # If admin account
        if self.is_admin(id_account):
            # PLACEHOLDER: navigate to Admin Landing page
            print('Successful admin login!')
        # Else (public account)
        else:
            # PLACEHOLDER: navigate to User Landing page
            print('Successful user login!')

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

    def verify_password(self, id_account, password):
        """
        Returns True if the given password matches the stored password for the Account. Returns False otherwise.

        :param int id_account: ID of the Account
        :param str password: target password
        :return: True if the passwords match, False otherwise
        """
        selectPassword_cmd = "SELECT password FROM Accounts WHERE id_account = %s"
        selectPassword_params = (id_account,)
        selectPassword_result = self.db.query(selectPassword_cmd, selectPassword_params)
        stored_password = selectPassword_result[0][0]
        return password == stored_password

    def is_admin(self, id_account):
        """
        Checks the credentials of the Account. Returns True if the Account is a administrative account, False otherwise (public account).

        :param int id_account: ID of the Account
        :return: True if the Account is an administrative account, False otherwise
        """
        selectCredentials_cmd = "SELECT id_credential FROM Accounts WHERE id_account = %s"
        selectCredentials_params = (id_account,)
        selectCredentials_result = self.db.query(selectCredentials_cmd, selectCredentials_params)
        credentials = selectCredentials_result[0][0]
        return credentials == 2


# --- Main Method --- #
if __name__ == "__main__":
    LoginBackend().run()