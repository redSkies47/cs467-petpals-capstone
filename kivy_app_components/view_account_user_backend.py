# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.app import App
from kivy.lang import Builder
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


# --- Main Method --- #
if __name__ == '__main__':
    ViewAccountBackend().run()
