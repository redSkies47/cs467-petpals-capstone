from kivy_app_components.admin_update_news import admin_update_news
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import os
from dotenv import load_dotenv
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu
from database.db_interface import Database
from database import animals_dml

# *** run through terminal from CS467-PETPALS-CAPSTONE: python -m kivy_app_components.sample_dropdown
# dropdown widget resource https://www.youtube.com/watch?v=6oHfaY6p0K0

# --- Set Up ---#

# Assign environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

class DEMO(FloatLayout):
    def drpdown_(self):
    # def drpdown_(self, instance):

        species_list = self.getSpecies()
        # print(len(species_list))
        self.menu_list = list()
        # for species in species_list:
        #     self.menu_list.append(
        #         {
        #         "viewclass":"OneLineListItem",
        #         "text":species[1],
        #         "on_release": lambda x = species[1] : self.notify(species[1])
        #     }
        #     )
        self.menu_list = [
            {
                "viewclass":"OneLineListItem",
                "text":species_list[0][1],
                "on_release": lambda x = species_list[0][1] : self.notify(species_list[0][1])
            },
            {
                "viewclass":"OneLineListItem",
                "text":species_list[1][1],
                "on_release": lambda x = species_list[1][1] : self.notify(species_list[1][1])
            },
                        {
                "viewclass":"OneLineListItem",
                "text":species_list[2][1],
                "on_release": lambda x = species_list[2][1] : self.notify(species_list[2][1])
            }
        ]

        self.menu = MDDropdownMenu (
            caller = self.ids.menu_,
            items = self.menu_list,
            width_mult = 2
        )

        # self.menu.caller = instance
        self.menu.open()

    def notify(self, item):
        print(item, "is pressed")

    def getSpecies(self):
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        species_object = animals_dml.get_species(self.db)
        return species_object

    Builder.load_file("../kv_design_language/sample_dropdown.kv")

class animal_sample(MDApp):

    def __init__(self, **kwargs):
        super(animal_sample, self).__init__(**kwargs)
        self.db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    def build(self):
        # for temporary rendering, expect screen to adapt to device res
        Window.size = (295, 620)
        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "LightBlue"
        # return Builder.load_file('../kv_design_language/sample_dropdown.kv')
        return DEMO()


if __name__ == '__main__':
    animal_sample().run()
