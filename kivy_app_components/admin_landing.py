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

# --- Set Up ---#

# Assign environment variables
# load_dotenv()

DB_HOST = "classmysql.engr.oregonstate.edu"
DB_USER = "capstone_2023_petpals"
DB_PASSWORD = "ph[r2cZ[QXqX9Ag8"
DB_NAME = "capstone_2023_petpals"
TOKEN = "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"
BRANCH = "main"

# local
DB_HOST = 'localhost'
DB_USER = 'shukie'
DB_PASSWORD = 'Gummyw0rm5!Gummy'
DB_NAME = 'capstone'
# local


TOKEN = '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'
BRANCH = "demo_instance"


class admin_landing(Screen):

    def __init__(self, **kwargs):
        super(admin_landing, self).__init__(**kwargs)
        self.DB_HOST = DB_HOST
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME
