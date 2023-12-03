from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import os
# from dotenv import load_dotenv
from database.db_interface import Database
from database.accounts_dml import *
from database import news_dml
# --- Set Up ---#

# Assign environment variables
# load_dotenv()
DB_HOST = "classmysql.engr.oregonstate.edu"
DB_USER = "capstone_2023_petpals"
DB_PASSWORD = "ph[r2cZ[QXqX9Ag8"
DB_NAME = "capstone_2023_petpals"
TOKEN = "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"

# local
DB_HOST = 'localhost'
DB_USER = 'shukie'
DB_PASSWORD = 'Gummyw0rm5!Gummy'
DB_NAME = 'capstone'
# local


TOKEN = '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'
BRANCH = "local_instance"


class admin_update_news(Screen):

    def __init__(self, **kwargs):
        super(admin_update_news, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        self.news = []
        self.curr_news = 0

    def getNews(self):
        news_object = news_dml.get_all_news(self.db)
        for news in news_object:
            curr_news = []
            for col in news:
                curr_news.append(col)
            self.news.append(curr_news)
        self.populateNews()

    def populateNews(self):
        self.ids.news_date.text = str(self.news[self.curr_news][1])
        self.ids.news_title.text = self.news[self.curr_news][2]
        self.ids.news_body.text = self.news[self.curr_news][3]

    def prev(self):
        self.curr_news = len(self.news) - \
            1 if self.curr_news == 0 else self.curr_news - 1
        self.populateNews()

    def next(self):
        self.curr_news = 0 if self.curr_news == len(
            self.news) - 1 else self.curr_news + 1
        self.populateNews()

    def toCancel(self):
        self.populateNews()

    def toSave(self):

        news_entry = self.news[self.curr_news][0]
        news_date = self.ids.news_date.text
        news_title = self.ids.news_title.text
        news_body = self.ids.news_body.text

        news_dml.update_one_news(
            news_entry, news_date, news_title, news_body, self.db)

        self.news[self.curr_news][1] = self.ids.news_date.text
        self.news[self.curr_news][2] = self.ids.news_title.text
        self.news[self.curr_news][3] = self.ids.news_body.text

    def toClear(self):
        self.ids.news_date.text = ""
        self.ids.news_title.text = ""
        self.ids.news_body.text = ""
