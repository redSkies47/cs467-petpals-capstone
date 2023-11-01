from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import os
from dotenv import load_dotenv
from database.db_interface import Database
from database.accounts_dml import *
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


class admin_update_news(Screen):

    # TODO: backend variables for metadata

    def toCancel(self):
        print("backend toCancel")
        # TODO: navigate to admin side - update news page
        # print(" ***backend user credentials: ", DB_HOST,
        #       DB_USER, DB_PASSWORD, DB_NAME)

    def toSave(self):
        # Builder.load_file('admin_update_news.kv')
        print("backend toSave")
        # TODO: navigate to admin side - add/edit animal page

    def toClear(self):
        print("backend toClear")
        # TODO: navigate to admin side - delete animal page
