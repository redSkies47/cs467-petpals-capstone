# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

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
Builder.load_file('../kv_design_language/create_account_user.kv')


# --- App Components --- #
class MainApp(App):
    """
    Represents the main app.
    """
    def build(self):
        return MyGridLayout()

class MyGridLayout(Widget):
    """
    Represents the Create Account page. Contains all of its structure and functionality.
    """
    # def __init__(self, **kwargs):
    #     super(MyGridLayout, self).__init__(**kwargs)

    #     self.cols = 1
    #     self.top_grid = GridLayout()
    #     self.top_grid.cols = 2

    #     self.top_grid.add_widget(Label(text="Email: "))
    #     self.email = TextInput(multiline=False)
    #     self.top_grid.add_widget(self.email)

    #     self.top_grid.add_widget(Label(text="Password: "))
    #     self.password = TextInput(multiline=False)
    #     self.top_grid.add_widget(self.password)

    #     self.add_widget(self.top_grid)

    #     self.login = Button(text="Login",
    #         font_size=30,
    #         size_hint_y = None,
    #         height = 75)
    #     self.login.bind(on_press=self.presslog)
    #     self.add_widget(self.login)

    #     self.account = Button(text="Create Account",
    #         font_size=30,
    #         size_hint_y = None,
    #         height = 75)
    #     self.account.bind(on_press=self.pressacc)
    #     self.add_widget(self.account)
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    name_input = ObjectProperty(None)       # account form - name field
    email_input = ObjectProperty(None)      # account form - email field
    password1_input = ObjectProperty(None)  # account form - password1 field
    password2_input = ObjectProperty(None)  # account form - password2 field

    def create_account(self):
        """
        Creates a new public Account. Successful creation if the required fields (email, password) are filled out correctly. Unsuccessful creation if any of the required fields are left blank, email is already registered, or passwords do not match.
        """
        name = self.name_input.text
        email = self.email_input.text
        password1 = self.password1_input.text
        password2 = self.password2_input.text

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

    def presslog(self):
        self.add_widget(Label(text="Login Successful"))

    def pressacc(self):
        self.add_widget(Label(text="One moment please"))


# --- Main Method --- #
if __name__ == '__main__':
    MainApp().run()