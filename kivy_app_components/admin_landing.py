from kivy_app_components.admin_update_news import admin_update_news
from kivy_app_components.admin_add_animal import admin_add_animal
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
        # for temporary rendering, expect screen to adapt to device res
        # Window.size = (295, 620)
        Window.size = (720, 1280)
        return Builder.load_file('../kv_design_language/admin_landing.kv')

    def toEditDeleteAnimal(self):
        print("Edit/Delete Animal")
        # admin_data_global.image_url += "admin_landing_"
        # print("*******************", admin_data_global.image_url)
        # TODO: navigate to admin side - delete animal page


if __name__ == '__main__':
    admin_landing().run()
