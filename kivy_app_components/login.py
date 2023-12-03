# --- Imports --- #
import kivy
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
import kivymd
from kivymd.app import MDApp

import database
from database.db_interface import Database
from database.accounts_dml import *


# --- Set Up ---#
DB_HOST = "classmysql.engr.oregonstate.edu"
DB_USER = "capstone_2023_petpals"
DB_PASSWORD = "ph[r2cZ[QXqX9Ag8"
DB_NAME = "capstone_2023_petpals"
TOKEN = "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"


# local
DB_HOST = 'localhost'
DB_USER = 'shukie'
DB_PASSWORD = 'Gummyw0rm5!Gummy'
DB_NAME = 'capstone'
# local


TOKEN = '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'
BRANCH = "demo_instance"


# --- App Components ---#
class MainApp(MDApp):
    """
    Represents the main app.
    """

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file('./kv_design_language/login.kv')


class LoginScreen(Screen):
    """
    Represents the Login page. Contains all of its structure and functionality.
    """

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    email_input = ObjectProperty(None)      # login form - email field
    password_input = ObjectProperty(None)   # login form - password field

    def login(self):
        """
        Validates login info. Successful login if the email and password match those of an Account. Unsuccessful login if the email is not registered or password is incorrect.
        """
        email = self.email_input.text
        password = self.password_input.text

        # If email is not registered
        accounts = find_account(email, self.db)
        if len(accounts) == 0:
            # PLACEHOLDER: error message
            print('Error: Failed to login. Email is not registered to an account.')
            return
        # If password is incorrect
        id_account = accounts[0][0]
        if not verify_password(id_account, password, self.db):
            # PLACEHOLDER: error message
            print('Error: Failed to login. Password is incorrect.')
            return

        # Successful login
        # If admin account
        if is_admin(id_account, self.db):
            # PLACEHOLDER: navigate to Admin Landing page
            print('Successful admin login!')
        # Else (public account)
        else:
            # PLACEHOLDER: navigate to User Landing page
            print('Successful user login!')


# --- Main Method --- #
if __name__ == "__main__":
    MainApp().run()
