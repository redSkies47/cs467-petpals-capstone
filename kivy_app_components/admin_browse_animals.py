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
from database import animals_dml
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from datetime import date
from textwrap import dedent
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button
import time
import random

# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


# local
DB_HOST = 'localhost'
DB_USER = 'shukie'
DB_PASSWORD = 'password'
DB_NAME = 'capstone'


class admin_browse_animals(Screen):

    def __init__(self, **kwargs):
        super(admin_browse_animals, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        self.image_link = ""
        self.species = []
        self.breeds = []
        self.gender = []
        self.availability = []
        self.dispositions = []
        self.curr_breed = 0
        self.curr_species = 1
        self.curr_gender = 1
        self.curr_availability = 1
        self.curr_disposition = 1
        self.dispositions_selection = []
        self.loaded_species_breeds = 0
        self.loaded_gender = 0
        self.loaded_availability = 0
        self.loaded_dispositions = 0

    def load_species_breeds(self):

        if self.loaded_species_breeds != 0:
            return
        self.loaded_species_breeds = 1
        self.species.append([])
        self.breeds.append([])
        species_table = animals_dml.get_species(self.db)
        for row in species_table:
            self.species.append(row[1])
            breeds_table = animals_dml.get_breed_by_species(row[0], self.db)
            if len(self.breeds) <= row[0]:
                self.breeds.append([])
            self.breeds[row[0]] = breeds_table

    def load_gender(self):

        if self.loaded_gender != 0:
            return
        self.loaded_gender = 1
        self.gender.append([])
        gender_table = animals_dml.get_genders(self.db)
        for row in gender_table:
            self.gender.append(row[1])

    def load_availability(self):
        if self.loaded_availability != 0:
            return
        self.loaded_availability = 1
        self.availability.append([])
        availability_table = animals_dml.get_availability(self.db)
        for row in availability_table:
            self.availability.append(row[1])

    def load_dispositions(self):

        if self.loaded_dispositions != 0:
            return
        self.loaded_dispositions = 1
        self.dispositions.append([])
        self.dispositions_selection.append(0)
        dispositions_table = animals_dml.get_dispositions(self.db)
        for row in dispositions_table:
            self.dispositions.append(row[1])
            self.dispositions_selection.append(0)

    def getImageURL(self):
        image_widget = self.ids.image_widget
        if not self.image_link:
            self.image_link = 'images/petpals_logo.png'
        image_widget.source = self.image_link

    def cancel(self):
        print("cancel")

    def save(self):
        availability = self.curr_availability
        name = str(self.ids.name.text)  # *
        birth_date = str(self.ids.birth_date.text)
        species = self.curr_species
        breed = int(self.breeds[self.curr_species][self.curr_breed][0])
        gender = int(self.curr_gender)
        summary = str(self.ids.summary.text)
        date_created = str(date.today())
        size = self.ids.size.text

        animals_dml.add_animal(availability,
                               species,
                               breed,
                               name,
                               birth_date,
                               gender,
                               size,
                               summary,
                               date_created,
                               self.db)

        animal_id = animals_dml.get_all_animals(self.db)[-1][0]
        for i in range(1, len(self.dispositions_selection)):
            if self.dispositions_selection[i] == 1:
                animals_dml.add_animal_disposition(animal_id, i, self.db)

        print("save")


# class FileChoose(Button):
#     '''
#     Button that triggers 'filechooser.open_file()' and processes
#     the data response from filechooser Activity.
#     '''

#     selection = ListProperty([])

#     def choose(self):
#         '''
#         Call plyer filechooser API to run a filechooser Activity.
#         '''
#         filechooser.open_file(on_selection=self.handle_selection)

#     def handle_selection(self, selection):
#         '''
#         Callback function for handling the selection response from Activity.
#         '''
#         self.selection = selection

#     def on_selection(self, *a, **k):
#         '''
#         Update TextInput.text after FileChoose.selection is changed
#         via FileChoose.handle_selection.
#         '''
#         # App.get_running_app().root.ids.result.text = str(self.selection)
#         pass
