# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import kivymd
from kivymd.app import MDApp

import database
from database.db_interface import Database
from database.accounts_dml import *
from database.news_dml import *


# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


# --- App Components ---#
class MainApp(App):
    def build(self):
        return Builder.load_file('../kv_design_language/user_front.kv')

class LoginScreen(MDApp):
    db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    id_account = None
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file('../kv_design_language/user_front.kv')

class LoginWindow(Screen):
    email_input = ObjectProperty(None)      # login form - email
    password_input = ObjectProperty(None)   # login form - password
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.bademail_label = Label(text='Error: Failed to login. Email is not registered to an account.',
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        self.badpass_label = Label(text='Error: Failed to login. Password is incorrect.',
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
    
    def clear_labels(self):
        if self.bademail_label:
            self.remove_widget(self.bademail_label)
        if self.badpass_label:
            self.remove_widget(self.badpass_label)

    def login(self):
        """
        Validates login info. Successful login if the email and password match those of an Account. Unsuccessful login if the email is not registered or password is incorrect.
        """
        email = self.email_input.text
        password = self.password_input.text
        def bad_email_label():
            self.add_widget(self.bademail_label)
        def bad_pass_label():
            self.add_widget(self.badpass_label)

        def clear_labels():
            if self.bademail_label:
                self.remove_widget(self.bademail_label)
            if self.badpass_label:
                self.remove_widget(self.badpass_label)
        # If email is not registered
        accounts = find_account(email, LoginScreen.db)
        if len(accounts) == 0:
            print('Error: Failed to login. Email is not registered to an account.')
            bad_email_label()
            return 
        # If password is incorrect
        id_account = accounts[0][0]
        if not verify_password(id_account, password, LoginScreen.db):
            clear_labels()
            print('Error: Failed to login. Password is incorrect.')
            bad_pass_label()
            return
        # Successful login
        # If admin account
        if is_admin(id_account, LoginScreen.db):
            # PLACEHOLDER: navigate to Admin Landing page
            print('Successful admin login!')
            clear_labels()
        # Else (public account)
        else:
            print('Successful user login!')
            clear_labels()
            self.manager.current = "landing"
            self.manager.transition.direction = "left"
        # Store id_account
        LoginScreen.id_account = id_account


class CreateAccountWindow(Screen):
    name_input = ObjectProperty(None)       # account form - name
    email_input = ObjectProperty(None)      # account form - email
    password1_input = ObjectProperty(None)  # account form - password
    password2_input = ObjectProperty(None)  # account form - confirm password
    def __init__(self, **kwargs):
        super(CreateAccountWindow, self).__init__(**kwargs)

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
        accounts = find_account(email, LoginScreen.db)
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
        add_account(email, password1, name, LoginScreen.db)
        # PLACEHOLDER: success message
        print('Successful account creation!')

class LandingWindow(Screen):
    name_input = ObjectProperty(None)       # update account form - name
    email_input = ObjectProperty(None)      # update account form - email
    password_input = ObjectProperty(None)   # update account form - password
    def __init__(self, **kwargs):
        (self.news_title, self.news_body) = self.get_news()
        self.change_label = Label(text="Changes Submitted!",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        self.delete_label = Label(text="Account Deleted.",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        super(LandingWindow, self).__init__(**kwargs)

    def get_news(self):
        """
        Returns a representation of the most recently added News item as a tuple (title, body).
        """
        news_item = get_all_news(LoginScreen.db)[-1]
        news_title = news_item[2]
        news_body = news_item[3]
        return (news_title, news_body)

    def update_account(self):
        """
        Updates the current Account. Unsuccessful update if the new email is already registered. Fields that are left blank are unmodified.
        """
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text

        # Update name, if entered
        if name != '':
            update_account_name(LoginScreen.id_account, name, LoginScreen.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account name!')
        # Update email, if entered
        if email != '':
            # If email is already registered
            accounts = find_account(email, LoginScreen.db)
            if len(accounts) > 0:
                # PLACEHOLDER: error message
                print('Error: Failed to update account email. Email is already registered to an account.')
            else:
                update_account_email(LoginScreen.id_account, email, LoginScreen.db)
                # PLACEHOLDER: success message
                print('Successfully updated the account email!')
        # Update password, if entered
        if password != '':
            update_account_password(LoginScreen.id_account, password, LoginScreen.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account password!')

    def delete_account(self):
        """
        Deletes the current Account.
        """
        # PLACEHOLDER: warning message
        print('Wait! Are you sure you want to delete this account?')

        # PLACEHOLDER: If confirmed yes... delete account
        delete_account(LoginScreen.id_account, LoginScreen.db)
        LoginScreen.id_account = None
        # PLACEHOLDER: success message
        print('Successfully deleted the account!')

    def logout(self):
        """
        Logs out of the current Account.
        """
        LoginScreen.id_account = None

    def press_change(self):
        self.add_widget(self.change_label)

    def press_delete(self):
        self.add_widget(self.delete_label)

    def clearchange(self):
        if self.change_label:
            self.remove_widget(self.change_label)
    def cleardelete(self):
        if self.delete_label:
            self.remove_widget(self.delete_label)

class WindowManager(ScreenManager):
    pass


# --- Main Method --- #
if __name__ == '__main__':
    LoginScreen().run()