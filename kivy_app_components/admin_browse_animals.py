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
from kivymd.uix.button import MDRectangleFlatButton
from datetime import date
from textwrap import dedent
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from io import BytesIO

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

# Assign Github variables
TOKEN = os.getenv('TOKEN')
DOMAIN = "https://github.com/"
REPO = "redSkies47/cs467-petpals-capstone"
REPO_PATH = "images/"
MESSAGE = "upload image"
BRANCH = "main"

# https://github.com/redSkies47/cs467-petpals-capstone/blob/admin_browse_animals/images/2.jpg

# DOMAIN + REPO + "/blob/" + BRANCH + "/images/" + id_image + ".jpg"


class admin_browse_animals_breed_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_browse_animals_breed_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_breed(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        curr_species = screen_main.curr_species
        breeds_list = screen_main.breeds
        curr_breed = screen_main.curr_breed
        curr_breed += 1
        if curr_breed >= len(breeds_list[curr_species]):
            curr_breed = 0
        self.set(screen_main, breeds_list, curr_species, curr_breed)

    def previous_breed(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
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
        screen_search = self.manager.get_screen(
            'admin_browse_animals_search_popup')
        screen_search.ids.breed.text = breeds_list[curr_species][curr_breed][1]
        screen_main.configured_breed = 1


class admin_browse_animals_species_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_browse_animals_species_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_species(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        species_list = screen_main.species
        curr_species = screen_main.curr_species
        curr_species += 1
        if curr_species >= len(species_list):
            curr_species = 0
        self.set(screen_main, species_list, curr_species)

    def previous_species(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        species_list = screen_main.species
        curr_species = screen_main.curr_species
        curr_species -= 1
        if curr_species < 0:
            curr_species = len(species_list) - 1
        self.set(screen_main, species_list, curr_species)

    def set(self, screen_main, species_list, curr_species):
        breeds_list = screen_main.breeds
        screen_main.curr_species = curr_species
        screen_main.curr_breed = 0
        self.ids.selection_species.text = species_list[curr_species]
        screen_search = self.manager.get_screen(
            'admin_browse_animals_search_popup')
        screen_search.ids.species.text = species_list[curr_species]
        screen_search.ids.breed.text = breeds_list[curr_species][0][1]
        # screen_search.ids.breed.text = 'Breed'
        screen_main.configured_species = 1


class admin_browse_animals_gender_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_browse_animals_gender_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_gender(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        gender_list = screen_main.gender
        curr_gender = screen_main.curr_gender
        curr_gender += 1
        if curr_gender >= len(gender_list):
            curr_gender = 0
        self.set(screen_main, gender_list, curr_gender)

    def previous_gender(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        gender_list = screen_main.gender
        curr_gender = screen_main.curr_gender
        curr_gender -= 1
        if curr_gender < 0:
            curr_gender = len(gender_list) - 1
        self.set(screen_main, gender_list, curr_gender)

    def set(self, screen_main, gender_list, curr_gender):
        # breeds_list = screen_main.breeds
        screen_main.curr_gender = curr_gender
        # screen_main.curr_breed = 0
        self.ids.selection_gender.text = gender_list[curr_gender]
        screen_search = self.manager.get_screen(
            'admin_browse_animals_search_popup')
        screen_search.ids.gender.text = gender_list[curr_gender]
        screen_main.configured_gender = 1


class admin_browse_animals_availability_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_browse_animals_availability_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def next_availability(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        availability_list = screen_main.availability
        curr_availability = screen_main.curr_availability
        curr_availability += 1
        if curr_availability >= len(availability_list):
            curr_availability = 0
        self.set(screen_main, availability_list, curr_availability)

    def previous_availability(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        availability_list = screen_main.availability
        curr_availability = screen_main.curr_availability
        curr_availability -= 1
        if curr_availability < 0:
            curr_availability = len(availability_list) - 1
        self.set(screen_main, availability_list, curr_availability)

    def set(self, screen_main, availability_list, curr_availability):
        # breeds_list = screen_main.breeds
        screen_main.curr_availability = curr_availability
        # screen_main.curr_breed = 0
        self.ids.selection_availability.text = availability_list[curr_availability]
        screen_search = self.manager.get_screen(
            'admin_browse_animals_search_popup')
        screen_search.ids.availability.text = availability_list[curr_availability]
        screen_main.configured_availability = 1


class admin_browse_animals_dispositions_popup(Screen):

    def __init__(self, **kwargs):
        super(admin_browse_animals_dispositions_popup, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        self.main_blue = (0/255, 187/255, 224/255, 1)
        light_gray = (171/255, 196/255, 212/255, 1)
        light_pink = (255/255, 233/255, 234/255, 1)
        self.select = [light_gray, light_pink]

    def next_disposition(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        dispositions_list = screen_main.dispositions
        curr_disposition = screen_main.curr_disposition
        curr_disposition += 1
        if curr_disposition >= len(dispositions_list):
            curr_disposition = 0
        self.set(screen_main, dispositions_list, curr_disposition)

    def previous_disposition(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
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
        screen_search = self.manager.get_screen(
            'admin_browse_animals_search_popup')
        screen_search.ids.dispositions.text = dispositions_list[curr_disposition]

    def toggle_select(self):
        screen_main = self.manager.get_screen(
            'admin_browse_animals')
        curr_disposition = screen_main.curr_disposition
        selection = screen_main.dispositions_selection
        if selection[curr_disposition] == 0:
            selection[curr_disposition] = 1
            self.ids.selection_dispositions.md_bg_color = self.select[1]
        else:
            selection[curr_disposition] = 0
            self.ids.selection_dispositions.md_bg_color = self.select[0]


class admin_browse_animals_search_popup(Screen):

    def search_popup(self):
        screen_main = self.manager.get_screen('admin_browse_animals')
        screen_main.search_main()


class admin_browse_animals(Screen):

    def __init__(self, **kwargs):
        super(admin_browse_animals, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        # self.image_link = ""
        self.species = []
        self.breeds = []
        self.gender = []
        self.availability = []
        self.dispositions = []
        self.curr_breed = 0
        self.curr_species = 0
        self.curr_gender = 0
        self.curr_availability = 0
        self.curr_disposition = 0
        self.dispositions_selection = []
        self.loaded_species_breeds = 0
        self.loaded_gender = 0
        self.loaded_availability = 0
        self.loaded_dispositions = 0
        self.configured_breed = 0
        self.configured_species = 0
        self.configured_gender = 0
        self.configured_availability = 0
        self.animals = None
        self.images = []

    def search_main(self):

        self.git_pull()

        species = self.curr_species
        breed = int(self.breeds[self.curr_species][self.curr_breed][0])
        gender = int(self.curr_gender)
        availability = self.curr_availability
        dispositions = self.dispositions_selection

        results = animals_dml.get_animals_by_species_breed_gender_availability_dispositions(species,
                                                                                            breed,
                                                                                            gender,
                                                                                            availability,
                                                                                            dispositions,
                                                                                            self.db)
        print(results)
        self.animals = results
        # print("***** len(self.animals): ", len(self.animals))
        # print("self.animals: ", self.animals)

        # for animal in self.animals:
        # print("***********animal: ", animal)
        self.images = []
        for num, animal in enumerate(self.animals):
            # print("***** animal[0]: ", animal[0])
            animal_images = animals_dml.get_all_images_by_id_animal(
                animal[0], self.db)
            image_list = []
            for image in animal_images:
                # image_link = DOMAIN + REPO + "/blob/" + \
                #     BRANCH + "/images/" + str(image[0]) + ".jpg"
                image_link = str(image[0])
                # print(image_link)
                image_list.append(image_link)
            self.images.append(image_list)

        # print("****** self.images", self.images)
        # print("****** len(self.images)", len(self.images))

        self.load_results()

    def load_results(self):

        results_container = self.ids.results_container
        for element in results_container.children:
            element.clear_widgets()
        results_container.clear_widgets()
        results_container.size_hint_y = (len(
            self.animals) + 1) / 2 * 1/4

        for num, animal in enumerate(self.animals):
            # print(" *** num: ", num)
            # print(" *** self.images[num][0]", self.images[num][0])
            pos_y_buff = num // 2
            center_x = 0.25 + 1/12 * 0.1 if num % 2 == 0 else 0.75 - 1/12 * 0.1
            size_h_y = 0.225 / self.ids.results_container.size_hint_y
            num_id = str(num)

            # fixed_x = int(self.ids.results_container.size_x)
            # fixed_y = int(self.ids.results_container.size_y)

            button = MDRectangleFlatButton(
                id=num_id,
                md_bg_color=(0/255, 0/255, 0/255, 0.1),
                line_color=(0/255, 0/255, 0/255, 0.5),
                size_hint_x=1/2 * 0.9,
                size_hint_y=size_h_y,
                # size_x=1/2 * 0.9 * fixed_x,
                # size_y=0.225 * fixed_y,
                # # size_hint_x=100,
                # size_hint_y=100,
                # size={"x": 1/2 * 0.9 * fixed_x, "y": 0.225 / \
                #       results_container_size_hiny_y * fixed_y},
                radius=[10, 10, 10, 10],
                pos_hint={"center_x": center_x, "center_y": 1 -
                          size_h_y * (11/18 + 10/9 * pos_y_buff)}
            )

            # bytes_io = BytesIO(self.images[num][0])

            image_dir = "./images/" + self.images[num][0] + ".jpg"
            print("********** image_dir: ", image_dir)

            image = AsyncImage(
                size_hint_x=4,
                size_hint_y=4,
                keep_ratio=False,
                allow_stretch=True,
                radius=[10, 10, 10, 10],
                source=image_dir,
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            )

            button.add_widget(image)
            results_container.add_widget(button)

        # self.ids.results_container.size_hint_y = MDFloatLayout.size_hint_y = math.ceil((num_animals) / 2) * 1/4  # extra row for space buffer
# pos_X_left = 0.25 + 1/12 * 0.1
# pos_x_right = 0.75 - 1/12 * 0.1
# size_hint_x = 1/2 * 0.9
# size_hint_y = 0.225 / self.parent.size_hint_y
#             = 0.225 / self.ids.results_container.size_hint_y
# pos_y = 1 - self.size_hint_y * (11/18 + 10/9 * animal_num // 2)

            #    MDRectangleFlatButton:
            #         md_bg_color: 0/255,0/255,0/255,0.1
            #         line_color: self.md_bg_color
            #         size_hint_x: 1/2 * 0.9
            #         size_hint_y: 0.225 / self.parent.size_hint_y
            #         radius: [10,10,10,10]
            #         pos_hint: {"center_x": 0.25 + 1/12 * 0.1 , "center_y": 1 - self.size_hint_y * (11/18 + 10/9 * 0// 2)}

            #         AsyncImage:
            #             id: image_widget
            #             size_hint_x: 1
            #             size_hint_y: 1
            #             keep_ratio: True
            #             allow_stretch: True
            #             # radius: [10,10,10,10]
            #             source: 'https://c8.alamy.com/comp/2BWX3PT/image-of-a-cute-stray-puppies-pictured-in-a-garbage-dump-2BWX3PT.jpg'
            #             pos_hint: {"center_x": 0.5, "center_y": 0.5}

    def load_species_breeds(self):

        if self.loaded_species_breeds != 0:
            return
        self.loaded_species_breeds = 1
        self.species.append('Species')
        self.breeds.append([(0, 'breed')])
        species_table = animals_dml.get_species(self.db)
        for row in species_table:
            self.species.append(row[1])
            breeds_table = animals_dml.get_breed_by_species(row[0], self.db)
            breeds_table.insert(0, (0, 'breed'))
            if len(self.breeds) <= row[0]:
                self.breeds.append([])
            self.breeds[row[0]] = breeds_table

        # print("species ", self.species)
        # print("breeds ", self.breeds)

    def load_gender(self):

        if self.loaded_gender != 0:
            return
        self.loaded_gender = 1
        self.gender.append('Gender')
        gender_table = animals_dml.get_genders(self.db)
        for row in gender_table:
            self.gender.append(row[1])

    def load_availability(self):
        if self.loaded_availability != 0:
            return
        self.loaded_availability = 1
        self.availability.append('Availability')
        availability_table = animals_dml.get_availability(self.db)
        for row in availability_table:
            self.availability.append(row[1])

    def load_dispositions(self):

        if self.loaded_dispositions != 0:
            return
        self.loaded_dispositions = 1
        self.dispositions.append('Dispositions')
        self.dispositions_selection.append(0)
        dispositions_table = animals_dml.get_dispositions(self.db)
        for row in dispositions_table:
            self.dispositions.append(row[1])
            self.dispositions_selection.append(0)

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
