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
from database import images
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
import subprocess

# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# # local
# DB_HOST = 'localhost'
# DB_USER = 'shukie'
# DB_PASSWORD = 'Gummyw0rm5!Gummy'
# DB_NAME = 'capstone'


# Assign Github variables
TOKEN = os.getenv('TOKEN')
DOMAIN = "https://github.com/"
REPO = "redSkies47/cs467-petpals-capstone"
REPO_PATH = "images/"
MESSAGE = "upload image"
BRANCH = "main"


class admin_add_animal_breed_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_add_animal_breed_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_breed(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        curr_species = screen_main.curr_species
        breeds_list = screen_main.breeds
        curr_breed = screen_main.curr_breed
        curr_breed += 1
        if curr_breed >= len(breeds_list[curr_species]):
            curr_breed = 0
        self.set(screen_main, breeds_list, curr_species, curr_breed)

    def previous_breed(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        curr_species = screen_main.curr_species
        breeds_list = screen_main.breeds
        curr_breed = screen_main.curr_breed
        curr_breed -= 1
        if curr_breed < 0:
            curr_breed = len(breeds_list[curr_species]) - 1
        self.set(screen_main, breeds_list, curr_species, curr_breed)

    def set(self, screen_main, breeds_list, curr_species, curr_breed):
        screen_main.curr_breed = curr_breed
        self.ids.selection_breed.text = breeds_list[curr_species][curr_breed][1]
        screen_main.ids.breed.text = breeds_list[curr_species][curr_breed][1]


class admin_add_animal_species_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_add_animal_species_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_species(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        species_list = screen_main.species
        curr_species = screen_main.curr_species
        curr_species += 1
        if curr_species >= len(species_list):
            curr_species = 1
        self.set(screen_main, species_list, curr_species)

    def previous_species(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        species_list = screen_main.species
        curr_species = screen_main.curr_species
        curr_species -= 1
        if curr_species < 1:
            curr_species = len(species_list) - 1
        self.set(screen_main, species_list, curr_species)

    def set(self, screen_main, species_list, curr_species):
        breeds_list = screen_main.breeds
        screen_main.curr_species = curr_species
        screen_main.curr_breed = 0
        self.ids.selection_species.text = species_list[curr_species]
        screen_main.ids.species.text = species_list[curr_species]
        screen_main.ids.breed.text = breeds_list[curr_species][0][1]


class admin_add_animal_gender_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_add_animal_gender_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_gender(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        gender_list = screen_main.gender
        curr_gender = screen_main.curr_gender
        curr_gender += 1
        if curr_gender >= len(gender_list):
            curr_gender = 1
        self.set(screen_main, gender_list, curr_gender)

    def previous_gender(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        gender_list = screen_main.gender
        curr_gender = screen_main.curr_gender
        curr_gender -= 1
        if curr_gender < 1:
            curr_gender = len(gender_list) - 1
        self.set(screen_main, gender_list, curr_gender)

    def set(self, screen_main, gender_list, curr_gender):
        # breeds_list = screen_main.breeds
        screen_main.curr_gender = curr_gender
        # screen_main.curr_breed = 0
        self.ids.selection_gender.text = gender_list[curr_gender]
        screen_main.ids.gender.text = gender_list[curr_gender]
        # screen_main.ids.breed.text = breeds_list[curr_species][0][1]


class admin_add_animal_availability_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_add_animal_availability_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_availability(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        availability_list = screen_main.availability
        curr_availability = screen_main.curr_availability
        curr_availability += 1
        if curr_availability >= len(availability_list):
            curr_availability = 1
        self.set(screen_main, availability_list, curr_availability)

    def previous_availability(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        availability_list = screen_main.availability
        curr_availability = screen_main.curr_availability
        curr_availability -= 1
        if curr_availability < 1:
            curr_availability = len(availability_list) - 1
        self.set(screen_main, availability_list, curr_availability)

    def set(self, screen_main, availability_list, curr_availability):
        # breeds_list = screen_main.breeds
        screen_main.curr_availability = curr_availability
        # screen_main.curr_breed = 0
        self.ids.selection_availability.text = availability_list[curr_availability]
        screen_main.ids.availability.text = availability_list[curr_availability]
        # screen_main.ids.breed.text = breeds_list[curr_species][0][1]


class admin_add_animal_shelter_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_add_animal_shelter_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_shelter(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        shelter_list = screen_main.shelter
        curr_shelter = screen_main.curr_shelter
        curr_shelter += 1
        if curr_shelter >= len(shelter_list):
            curr_shelter = 1
        self.set(screen_main, shelter_list, curr_shelter)

    def previous_shelter(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        shelter_list = screen_main.shelter
        curr_shelter = screen_main.curr_shelter
        curr_shelter -= 1
        if curr_shelter < 1:
            curr_shelter = len(shelter_list) - 1
        self.set(screen_main, shelter_list, curr_shelter)

    def set(self, screen_main, shelter_list, curr_shelter):
        # breeds_list = screen_main.breeds
        screen_main.curr_shelter = curr_shelter
        # screen_main.curr_breed = 0
        self.ids.selection_shelter.text = shelter_list[curr_shelter]
        screen_main.ids.shelter.text = shelter_list[curr_shelter]
        # screen_main.ids.breed.text = breeds_list[curr_species][0][1]


class admin_add_animal_dispositions_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_add_animal_dispositions_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        self.main_blue = (0/255, 187/255, 224/255, 1)
        light_gray = (171/255, 196/255, 212/255, 1)
        light_pink = (255/255, 233/255, 234/255, 1)
        self.select = [light_gray, light_pink]

    def next_disposition(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        dispositions_list = screen_main.dispositions
        curr_disposition = screen_main.curr_disposition
        curr_disposition += 1
        if curr_disposition >= len(dispositions_list):
            curr_disposition = 1
        self.set(screen_main, dispositions_list, curr_disposition)

    def previous_disposition(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        dispositions_list = screen_main.dispositions
        curr_disposition = screen_main.curr_disposition
        curr_disposition -= 1
        if curr_disposition < 1:
            curr_disposition = len(dispositions_list) - 1
        self.set(screen_main, dispositions_list, curr_disposition)

    def set(self, screen_main, dispositions_list, curr_disposition):
        screen_main.curr_disposition = curr_disposition
        self.ids.selection_dispositions.text = dispositions_list[curr_disposition]
        self.ids.selection_dispositions.md_bg_color = self.select[
            screen_main.dispositions_selection[curr_disposition]]
        screen_main.ids.dispositions.text = dispositions_list[curr_disposition]

    def toggle_select(self):
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        curr_disposition = screen_main.curr_disposition
        selection = screen_main.dispositions_selection
        if selection[curr_disposition] == 0:
            selection[curr_disposition] = 1
            self.ids.selection_dispositions.md_bg_color = self.select[1]
        else:
            selection[curr_disposition] = 0
            self.ids.selection_dispositions.md_bg_color = self.select[0]


class admin_add_animal_url_popup(Screen):

    def load_image(self):
        # print("popup")
        screen_main = self.manager.get_screen(
            'admin_add_animal')
        screen_main.image_link = self.ids.image_url.text
        screen_main.getImageURL()


class admin_add_animal(Screen):

    def __init__(self, **kwargs):
        super(admin_add_animal, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        self.image_link = ""
        self.species = []
        self.breeds = []
        self.gender = []
        self.availability = []
        self.shelter = []
        self.dispositions = []
        self.curr_breed = 0
        self.curr_species = 1
        self.curr_gender = 1
        self.curr_availability = 1
        self.curr_shelter = 1
        self.curr_disposition = 1
        self.dispositions_selection = []
        self.loaded_species_breeds = 0
        self.loaded_gender = 0
        self.loaded_availability = 0
        self.loaded_shelter = 0
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

        # print(self.species)
        # print(self.breeds)

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

    def load_shelter(self):
        if self.loaded_shelter != 0:
            return
        self.loaded_shelter = 1
        self.shelter.append([])
        shelter_table = animals_dml.get_shelters(self.db)
        for row in shelter_table:
            self.shelter.append(row[1])

    def load_default(self):
        self.load_species_breeds()
        self.load_gender()
        self.load_availability()
        self.load_dispositions()
        self.load_shelter()

    def getImageURL(self):
        image_widget = self.ids.image_widget
        if not self.image_link:
            self.image_link = 'images/petpals_logo.png'
        image_widget.source = self.image_link

    # def cancel(self):
    #     self.reset_all()
    #     print("canceled")

    def save(self):

        name = str(self.ids.name.text)
        birth_date = str(self.ids.birth_date.text)
        summary = str(self.ids.summary.text)
        size = str(self.ids.size.text)
        image = self.image_link

        name_valid = name != "NAME"
        bith_date_valid = birth_date != "BIRTH DATE"
        summary_valid = summary != ''
        size_valid = size != ''
        image_valid = image != ''

        if not (name_valid and bith_date_valid and summary_valid and size_valid and image_valid):
            self.manager.current = "admin_add_animal_warning_popup"
            return

        self.manager.current = "admin_add_animal_loading_popup"

        availability = self.curr_availability
        name = str(self.ids.name.text)
        birth_date = str(self.ids.birth_date.text)
        species = self.curr_species
        breed = int(self.breeds[self.curr_species][self.curr_breed][0])
        gender = int(self.curr_gender)
        summary = str(self.ids.summary.text)
        date_created = str(date.today())
        shelter = self.curr_shelter
        size = self.ids.size.text

        # print("*** shelter: ", shelter)
        add_res = animals_dml.add_animal(availability,
                                         species,
                                         breed,
                                         name,
                                         birth_date,
                                         gender,
                                         size,
                                         summary,
                                         date_created,
                                         shelter,
                                         self.db)

        # print("*** add res: ", add_res)
        animal_id = animals_dml.get_all_animals(self.db)[-1][0]
        for i in range(1, len(self.dispositions_selection)):
            if self.dispositions_selection[i] == 1:
                animals_dml.add_animal_disposition(animal_id, i, self.db)

        added_animal = animals_dml.get_all_animals(self.db)[-1]
        # print("**** all animals: ", added_animal)

        # test
        id_animal = int(added_animal[0])

        # id_animal = animals_dml.get_all_animals(self.db)[-1][0]
        # print("***** id_animal: ", id_animal)

        images.upload_and_save_image(id_animal, self.image_link, self.db)
        self.git_pull()

        self.manager.current = "admin_add_animal_saved_popup"
        self.reset_all()
        print("saved")

    def reset_all(self):

        self.curr_breed = 0
        self.curr_species = 1
        self.curr_gender = 1
        self.curr_availability = 1
        self.curr_shelter = 1
        self.curr_disposition = 1
        self.dispositions_selection = []
        self.image_link = 'images/petpals_logo.png'

        screen_search = self.manager.get_screen(
            'admin_add_animal')
        # screen_search.ids.breed.text = self.breeds[self.curr_species][self.curr_breed][1]
        # screen_search.ids.species.text = self.species[self.curr_species]
        # screen_search.ids.gender.text = self.gender[self.curr_gender]
        # screen_search.ids.availability.text = self.availability[self.curr_availability]
        # screen_search.ids.dispositions.text = self.dispositions[self.curr_disposition]
        # screen_search.ids.shelter.text = self.shelter[self.curr_shelter]
        screen_search.ids.breed.text = 'BREED'
        screen_search.ids.species.text = 'SPECIES'
        screen_search.ids.gender.text = 'GENDER'
        screen_search.ids.availability.text = 'AVAILABILITY'
        screen_search.ids.dispositions.text = 'DISPOSITIONS'
        screen_search.ids.shelter.text = 'SHELTER'

        # screen_species = self.manager.get_screen(
        #     'admin_add_animal_species_popup')
        # screen_species.ids.selection_species.text = self.species[self.curr_species]
        # screen_breed = self.manager.get_screen(
        #     'admin_add_animal_breed_popup')
        # screen_breed.ids.selection_breed.text = self.breeds[self.curr_species][self.curr_breed][1]
        # screen_gender = self.manager.get_screen(
        #     'admin_add_animal_gender_popup')
        # screen_gender.ids.selection_gender.text = self.gender[self.curr_gender]
        # screen_availability = self.manager.get_screen(
        #     'admin_add_animal_availability_popup')
        # screen_availability.ids.selection_availability.text = self.availability[
        #     self.curr_availability]
        # screen_dispositions = self.manager.get_screen(
        #     'admin_add_animal_shelter_popup')
        # screen_dispositions.ids.selection_shelter.text = self.shelter[
        #     self.curr_shelter]
        # screen_url = self.manager.get_screen('admin_add_animal_url_popup')
        # screen_url.ids.image_url.text = ''
        screen_species = self.manager.get_screen(
            'admin_add_animal_species_popup')
        screen_species.ids.selection_species.text = 'SPECIES'
        screen_breed = self.manager.get_screen(
            'admin_add_animal_breed_popup')
        screen_breed.ids.selection_breed.text = 'BREED'
        screen_gender = self.manager.get_screen(
            'admin_add_animal_gender_popup')
        screen_gender.ids.selection_gender.text = 'GENDER'
        screen_availability = self.manager.get_screen(
            'admin_add_animal_availability_popup')
        screen_availability.ids.selection_availability.text = 'AVAILABILITY'
        screen_shelter = self.manager.get_screen(
            'admin_add_animal_shelter_popup')
        screen_shelter.ids.selection_shelter.text = 'SHELTER'
        screen_url = self.manager.get_screen('admin_add_animal_url_popup')
        screen_url.ids.image_url.text = ''
        screen_dispositions = self.manager.get_screen(
            'admin_add_animal_dispositions_popup')
        screen_dispositions.ids.selection_dispositions.text = 'DISPOSITIONS'
        screen_dispositions.ids.selection_dispositions.md_bg_color = (
            171/255, 196/255, 212/255, 1)

        self.ids.name.text = 'NAME'
        self.ids.birth_date.text = 'BIRTH DATE'
        self.ids.summary.text = ''
        self.ids.size.text = 'SIZE'
        self.ids.image_widget.source = self.image_link

        self.species = []
        self.breeds = []
        self.gender = []
        self.availability = []
        self.dispositions = []
        self.dispositions_selection = []
        self.shelter = []
        self.loaded_species_breeds = 0
        self.loaded_gender = 0
        self.loaded_availability = 0
        self.loaded_dispositions = 0
        self.loaded_shelter = 0
        print("reset all")

    def git_pull(repository_path):
        try:
            repo = DOMAIN + REPO
            branch = BRANCH
            main_dir = '/home/shukie/Documents/CS467/cs467-petpals-capstone'
            subprocess.run(['cd', main_dir], shell=True)
            command = f'git pull {repo} {branch}'
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True)
            print("Git pull successful. ", result)
        except subprocess.CalledProcessError as e:
            print(f"Error during git pull: {e}")


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
