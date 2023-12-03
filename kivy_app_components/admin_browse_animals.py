from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import os
# from dotenv import load_dotenv
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
from datetime import datetime

import time
import random
import subprocess
# --- Set Up ---#

# Assign environment variables
# load_dotenv()
DB_HOST = "classmysql.engr.oregonstate.edu"
DB_USER = "capstone_2023_petpals"
DB_PASSWORD = "ph[r2cZ[QXqX9Ag8"
DB_NAME = "capstone_2023_petpals"

# Assign Github variables
TOKEN = os.getenv('TOKEN')
DOMAIN = "https://github.com/"
REPO = "redSkies47/cs467-petpals-capstone"
REPO_PATH = "images/"
MESSAGE = "upload image"
BRANCH = "main"

# local
DB_HOST = 'localhost'
DB_USER = 'shukie'
DB_PASSWORD = 'Gummyw0rm5!Gummy'
DB_NAME = 'capstone'
# local


TOKEN = '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'
BRANCH = "demo_instace"


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
        # screen_main.configured_breed = 1


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
        # print(
        #     "************ species_list[curr_species] ", species_list[curr_species], self.ids.selection_species)

        self.ids.selection_species.text = species_list[curr_species]
        screen_search = self.manager.get_screen(
            'admin_browse_animals_search_popup')
        screen_search.ids.species.text = species_list[curr_species]
        screen_search.ids.breed.text = breeds_list[curr_species][0][1]
        # screen_search.ids.breed.text = 'Breed'
        # screen_main.configured_species = 1


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
        # screen_main.configured_gender = 1


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
        # screen_main.configured_availability = 1


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
        screen_main.load_all()
        # screen_main.search_main()


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
        self.curr_animal = 0
        self.dispositions_selection = []
        self.loaded_species_breeds = 0
        self.loaded_gender = 0
        self.loaded_availability = 0
        self.loaded_dispositions = 0
        self.animals = None
        self.images = []
        self.loaded_default = 0

    def load_default(self):
        if self.loaded_default == 1:
            return
        self.loaded_default = 1
        self.load_all()

    def load_all(self):
        self.manager.current = "admin_browse_animals_loading_popup"
        self.load_species_breeds()
        self.load_gender()
        self.load_availability()
        self.load_dispositions()
        self.search_main()
        self.manager.current = "admin_browse_animals"

    def reset_all(self):

        self.curr_breed = 0
        self.curr_species = 0
        self.curr_gender = 0
        self.curr_availability = 0
        self.curr_disposition = 0

        screen_search = self.manager.get_screen(
            'admin_browse_animals_search_popup')
        screen_search.ids.breed.text = self.breeds[self.curr_species][self.curr_breed][1]
        screen_search.ids.species.text = self.species[self.curr_species]
        screen_search.ids.gender.text = self.gender[self.curr_gender]
        screen_search.ids.availability.text = self.availability[self.curr_availability]
        screen_search.ids.dispositions.text = self.dispositions[self.curr_disposition]
        screen_species = self.manager.get_screen(
            'admin_browse_animals_species_popup')
        screen_species.ids.selection_species.text = self.species[self.curr_species]
        screen_breed = self.manager.get_screen(
            'admin_browse_animals_breed_popup')
        screen_breed.ids.selection_breed.text = self.breeds[self.curr_species][self.curr_breed][1]
        screen_gender = self.manager.get_screen(
            'admin_browse_animals_gender_popup')
        screen_gender.ids.selection_gender.text = self.gender[self.curr_gender]
        screen_availability = self.manager.get_screen(
            'admin_browse_animals_availability_popup')
        screen_availability.ids.selection_availability.text = self.availability[
            self.curr_availability]
        screen_dispositions = self.manager.get_screen(
            'admin_browse_animals_dispositions_popup')
        screen_dispositions.ids.selection_dispositions.text = self.dispositions[
            self.curr_disposition]

        self.species = []
        self.breeds = []
        self.gender = []
        self.availability = []
        self.dispositions = []
        self.dispositions_selection = []
        self.loaded_species_breeds = 0
        self.loaded_gender = 0
        self.loaded_availability = 0
        self.loaded_dispositions = 0
        self.animals = None
        self.images = []

        self.loaded_default = 0

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

            print("********** num_id: ", num_id)

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
                          size_h_y * (11/18 + 10/9 * pos_y_buff)},
                on_release=lambda this_button: self.to_admin_edit_delete_animal(
                    this_button.id),
                on_load=lambda this_button: button_dimensions(this_button)
            )

            def button_dimensions(button):
                button.size_hint_x = button.parent.parent.width * 9
                button.size_hint_y = button.parent.parent.height * 9

            # bytes_io = BytesIO(self.images[num][0])

            print("###### self.images:", self.images)
            image_dir = "./images/" + self.images[num][0] + ".jpg"
            # print("********** image_dir: ", image_dir)

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

    def to_admin_landing(self):
        self.reset_all()
        self.manager.current = "admin_landing"

    def to_admin_edit_delete_animal(self, animal_index):

        self.manager.current = "admin_browse_animals_loading_popup"
        print("***** animal_index: ", animal_index)
        self.curr_animal = int(animal_index)
        screen_ed_animal = self.manager.get_screen("admin_edit_delete_animal")
        # print(screen_ed_animal)
        screen_ed_animal.load_default()
        selected_animal = self.animals[self.curr_animal]
        print("********* selected_animal: ", selected_animal)

        #         self.curr_breed = 0
        # self.curr_species = 1
        # self.curr_gender = 1
        # self.curr_availability = 1
        # self.curr_shelter = 1
        # self.curr_disposition = 1
        # self.dispositions_selection = []
        #  [(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, id_shelter, list(id_dispositions))]
        screen_ed_animal.curr_animal_id = selected_animal[0]
        screen_ed_animal.curr_availability = selected_animal[1]
        screen_ed_animal.curr_species = selected_animal[2]

        screen_ed_animal.curr_breed = selected_animal[3]
        screen_ed_animal.curr_name = selected_animal[4]
        screen_ed_animal.curr_bday = selected_animal[5].strftime("%Y/%m/%d")
        screen_ed_animal.curr_gender = selected_animal[6]
        screen_ed_animal.curr_size = selected_animal[7]
        screen_ed_animal.curr_summary = selected_animal[8]
        screen_ed_animal.curr_cday = selected_animal[9].strftime("%Y/%m/%d")
        screen_ed_animal.curr_shelter = selected_animal[10]

        curr_animal_dispositions = []
        if selected_animal[11]:
            curr_animal_dispositions = sorted([int(i)
                                               for i in selected_animal[11].split(',')])
        print(screen_ed_animal.curr_cday)
        print(screen_ed_animal.curr_bday)
        print(curr_animal_dispositions)

        curr_dispositions_selection = []
        i = 0
        max = len(self.dispositions_selection) - 1
        for disposition in curr_animal_dispositions:
            print(disposition)
            for j in range(disposition-i):
                curr_dispositions_selection.append(0)
            curr_dispositions_selection.append(1)
            i = disposition + 1
        while i < len(self.dispositions_selection):
            curr_dispositions_selection.append(0)
            i += 1

        print(curr_dispositions_selection)
        screen_ed_animal.dispositions_selection = curr_dispositions_selection
        screen_ed_animal.curr_disposition = 1

        screen_ed_animal.set_animal()
        self.manager.current = "admin_edit_delete_animal"

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
