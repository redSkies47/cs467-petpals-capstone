# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

import database
from database.db_interface import Database
from database.news_dml import *


# --- Set Up --- #

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Load kv files
Builder.load_file('../kv_design_language/landing_page_user_backend.kv')


# --- App Components --- #
class LandingBackend(App):
    """
    Represents the Landing page.
    """
    def build(self):
        return LandingBoxLayout()


class LandingBoxLayout(Widget):
    """
    Contains the structure and functionality of the Landing page.
    """
    def __init__(self, **kwargs):
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        (self.news_title, self.news_body) = self.get_news()
        super(LandingBoxLayout, self).__init__(**kwargs)

    def get_news(self):
        """
        Returns a representation of the most recently added News item as a tuple (title, body).
        """
        news_item = get_all_news(self.db)[-1]
        news_title = news_item[2]
        news_body = news_item[3]
        return (news_title, news_body)


# --- Main Method --- #
if __name__ == '__main__':
    LandingBackend().run()
