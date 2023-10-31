# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

import database
from database.db_interface import Database
from database.accounts_dml import *


# --- Set Up --- #

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Load kv files
Builder.load_file('../kv_design_language/view_account_user_backend.kv')


# --- App Components --- #
class ViewAccountBackend(App):
    """
    Represents the View Account page.
    """
    def build(self):
        return ViewAccountBoxLayout()


class ViewAccountBoxLayout(Widget):
    """
    Contains the structure and functionality of the View Account page.
    """
    def __init__(self, **kwargs):
        super(ViewAccountBoxLayout, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        # TODO: retrieve stored information from logging in
        self.id_account = 4

    name_input = ObjectProperty(None)
    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)

    def update_account(self):
        """
        Updates the current Account. Unsuccessful update if the new email is already registered. Fields that are left blank are unmodified.
        """
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text

        # Update name, if entered
        if name != '':
            update_account_name(self.id_account, name, self.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account name!')
        # Update email, if entered
        if email != '':
            # If email is already registered
            accounts = find_account(email, self.db)
            if len(accounts) > 0:
                # PLACEHOLDER: error message
                print('Error: Failed to update account email. Email is already registered to an account.')
            else:
                update_account_email(self.id_account, email, self.db)
                # PLACEHOLDER: success message
                print('Successfully updated the account email!')
        # Update password, if entered
        if password != '':
            update_account_password(self.id_account, password, self.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account password!')

    def delete_account(self):
        """
        Deletes the current Account.
        """
        # PLACEHOLDER: warning message
        print('Wait! Are you sure you want to delete this account?')

        # If confirmed yes... delete account
        delete_account(self.id_account, self.db)
        # PLACEHOLDER: success message
        print('Successfully deleted the account!')


# --- Main Method --- #
if __name__ == '__main__':
    ViewAccountBackend().run()
