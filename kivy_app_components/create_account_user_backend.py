# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

import database
from database.db_interface import Database
from database.accounts_dml import *


# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Load kv files
Builder.load_file('../kv_design_language/create_account_user_backend.kv')


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
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

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
        accounts = find_account(email, self.db)
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
        add_account(email, password1, name, self.db)
        # PLACEHOLDER: success message
        print('Successful account creation!')


# --- Main Method --- #
if __name__ == "__main__":
    CreateAccountUserBackend().run()
