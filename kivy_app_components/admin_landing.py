from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import os
# from dotenv import load_dotenv
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from database.db_interface import Database
from database.accounts_dml import *
from database.credentials import *

# --- Set Up ---#

# Assign environment variables
# load_dotenv()


BRANCH = "main"


class admin_landing(Screen):

    def __init__(self, **kwargs):
        super(admin_landing, self).__init__(**kwargs)
        self.DB_HOST = DB_HOST
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME
