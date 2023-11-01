from kivy_app_components.admin_update_news import admin_update_news
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import os
from dotenv import load_dotenv
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from database.db_interface import Database
from database.accounts_dml import *

# *** run through terminal from CS467-PETPALS-CAPSTONE: python3 -m kivy_app_components.admin_landing

# --- Set Up ---#

# Assign environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


class admin_landing(MDApp):

    def __init__(self, **kwargs):
        super(admin_landing, self).__init__(**kwargs)
        self.DB_HOST = DB_HOST
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME

    def build(self):
        Window.size = (295, 620)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file('../kv_design_language/admin_landing.kv')

    def toUpdateNews(self):
        print("Update News")
        # TODO: navigate to admin side - update news page

    def toAddAnimal(self):
        print("Add Animal")
        print(" ***backend user credentials: ", self.DB_HOST,
              self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        # TODO: navigate to admin side - add/edit animal page

    def toEditDeleteAnimal(self):
        print("Edit/Delete Animal")
        # TODO: navigate to admin side - delete animal page


if __name__ == '__main__':
    admin_landing().run()
