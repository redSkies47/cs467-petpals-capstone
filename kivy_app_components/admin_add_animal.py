from plyer import filechooser
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import os
from dotenv import load_dotenv
from database.db_interface import Database
from database.accounts_dml import *
from database import news_dml
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from textwrap import dedent

# from plyer import filechooser

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button

# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


class admin_add_animal_url_popup(Screen):

    def load_image(self):
        print("popup")
        admin_add_animal.image_link = self.ids.image_url.text
        screen_admin_add_animal = self.manager.get_screen('admin_add_animal')
        screen_admin_add_animal.load_image1()


class admin_add_animal(Screen):

    image_link = ""

    def __init__(self, **kwargs):
        super(admin_add_animal, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def load_image1(self):
        image_widget = self.ids.image_widget
        image_url_widget = self.ids.image_url
        if not admin_add_animal.image_link:
            admin_add_animal.image_link = 'images/petpals_logo.png'
        image_widget.source = admin_add_animal.image_link

    def cancel(self):
        print("cancel")

    def save(self):
        print("save")

    def menu_open(self):

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "1",
                "on_release": lambda x="1": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "2",
                "on_release": lambda x="2": self.menu_callback(x),
            }
        ]
        MDDropdownMenu(
            caller=self.ids.button, items=menu_items
        ).open()

    def menu_callback(self, text_item):
        print(text_item)


class FileChoose(Button):
    '''
    Button that triggers 'filechooser.open_file()' and processes
    the data response from filechooser Activity.
    '''

    selection = ListProperty([])

    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        # App.get_running_app().root.ids.result.text = str(self.selection)
        pass
