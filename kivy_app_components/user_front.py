# --- Imports --- #
import os
from dotenv import load_dotenv

import kivy
from kivy.lang import Builder
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton
import kivymd
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty

import database
from database.db_interface import Database
from database.accounts_dml import *
from database.news_dml import *
from database.animals_dml import *


# --- Set Up ---#

# Assign environment variables
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


# --- App Components ---#
class MainApp(MDApp):
    db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    id_account = None
    def build(self):
        Window.size = (720, 1280)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file('../kv_design_language/user_front.kv')

class LoginWindow(Screen):
    email_input = ObjectProperty(None)      # login form - email
    password_input = ObjectProperty(None)   # login form - password
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.bademail_label = Label(text='Error: Failed to login. Email is not registered to an account.',
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        self.badpass_label = Label(text='Error: Failed to login. Password is incorrect.',
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})

    def clear_labels(self):
        if self.bademail_label:
            self.remove_widget(self.bademail_label)
        if self.badpass_label:
            self.remove_widget(self.badpass_label)

    def login(self):
        """
        Validates login info. Successful login if the email and password match those of an Account. Unsuccessful login if the email is not registered or password is incorrect.
        """
        email = self.email_input.text
        password = self.password_input.text
        def bad_email_label():
            self.add_widget(self.bademail_label)
        def bad_pass_label():
            self.add_widget(self.badpass_label)

        def clear_labels():
            if self.bademail_label:
                self.remove_widget(self.bademail_label)
            if self.badpass_label:
                self.remove_widget(self.badpass_label)
        # If email is not registered
        accounts = find_account(email, MainApp.db)
        if len(accounts) == 0:
            print('Error: Failed to login. Email is not registered to an account.')
            bad_email_label()
            return
        # If password is incorrect
        id_account = accounts[0][0]
        if not verify_password(id_account, password, MainApp.db):
            clear_labels()
            print('Error: Failed to login. Password is incorrect.')
            bad_pass_label()
            return
        # Successful login
        # If admin account
        if is_admin(id_account, MainApp.db):
            # PLACEHOLDER: navigate to Admin Landing page
            print('Successful admin login!')
            clear_labels()
        # Else (public account)
        else:
            print('Successful user login!')
            clear_labels()
            self.manager.current = "landing"
            self.manager.transition.direction = "left"
        # Store id_account
        MainApp.id_account = id_account


class CreateAccountWindow(Screen):
    name_input = ObjectProperty(None)       # account form - name
    email_input = ObjectProperty(None)      # account form - email
    password1_input = ObjectProperty(None)  # account form - password
    password2_input = ObjectProperty(None)  # account form - confirm password
    def __init__(self, **kwargs):
        super(CreateAccountWindow, self).__init__(**kwargs)

    def create_account(self):
        """
        Creates a new public Account. Successful creation if the required fields (email, password) are filled out correctly. Unsuccessful creation if any of the required fields are left blank, email is already registered, or passwords do not match.
        """
        name = self.name_input.text
        email = self.email_input.text
        password1 = self.password1_input.text
        password2 = self.password2_input.text

        # If any required fields are left blank
        if email == '' or password1 == '' or password2 == '':
            # PLACEHOLDER: error message
            print('Error: Failed to create account. Missing required field(s).')
            return
        # If email is already registered
        accounts = find_account(email, MainApp.db)
        if len(accounts) > 0:
            # PLACEHOLDER: error message
            print('Error: Failed to create account. Email is already registered to an account.')
            return
        # If passwords do not match
        if password1 != password2:
            # PLACEHOLDER: error message
            print('Error: Failed to create account. Passwords do not match.')
            return

        # Create account
        add_account(email, password1, name, MainApp.db)
        # PLACEHOLDER: success message
        print('Successful account creation!')

class LandingWindow(Screen):
    name_input = ObjectProperty(None)       # update account form - name
    email_input = ObjectProperty(None)      # update account form - email
    password_input = ObjectProperty(None)   # update account form - password
    def __init__(self, **kwargs):
        (self.news_title, self.news_body) = self.get_news()
        self.change_label = Label(text="Changes Submitted!",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        self.delete_label = Label(text="Account Deleted.",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        super(LandingWindow, self).__init__(**kwargs)

    def get_news(self):
        """
        Returns a representation of the most recently added News item as a tuple (title, body).
        """
        news_item = get_all_news(MainApp.db)[-1]
        news_title = news_item[2]
        news_body = news_item[3]
        return (news_title, news_body)

    def update_account(self):
        """
        Updates the current Account. Unsuccessful update if the new email is already registered. Fields that are left blank are unmodified.
        """
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text

        # Update name, if entered
        if name != '':
            update_account_name(MainApp.id_account, name, MainApp.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account name!')
        # Update email, if entered
        if email != '':
            # If email is already registered
            accounts = find_account(email, MainApp.db)
            if len(accounts) > 0:
                # PLACEHOLDER: error message
                print('Error: Failed to update account email. Email is already registered to an account.')
            else:
                update_account_email(MainApp.id_account, email, MainApp.db)
                # PLACEHOLDER: success message
                print('Successfully updated the account email!')
        # Update password, if entered
        if password != '':
            update_account_password(MainApp.id_account, password, MainApp.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account password!')

    def delete_account(self):
        """
        Deletes the current Account.
        """
        # PLACEHOLDER: warning message
        print('Wait! Are you sure you want to delete this account?')

        # PLACEHOLDER: If confirmed yes... delete account
        delete_account(MainApp.id_account, MainApp.db)
        MainApp.id_account = None
        # PLACEHOLDER: success message
        print('Successfully deleted the account!')

    def logout(self):
        """
        Logs out of the current Account.
        """
        MainApp.id_account = None

    def press_change(self):
        self.add_widget(self.change_label)

    def press_delete(self):
        self.add_widget(self.delete_label)

    def clearchange(self):
        if self.change_label:
            self.remove_widget(self.change_label)
    def cleardelete(self):
        if self.delete_label:
            self.remove_widget(self.delete_label)

class DogBrowseWindow(Screen):
    name_input = ObjectProperty(None)       # update account form - name
    email_input = ObjectProperty(None)      # update account form - email
    password_input = ObjectProperty(None)   # update account form - password

    def __init__(self, **kwargs):
        (self.news_title, self.news_body) = self.get_news()
        self.change_label = Label(text="Changes Submitted!",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        self.delete_label = Label(text="Account Deleted. Please Log Out.",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        self.no_results_label = Label(text="No matches were found!",
                              color = (255/255, 0/255, 0/255, 1),
                              size_hint = (.2,.2),
                              font_size = self.width/2,
                              pos_hint = {"center_x": 0.5, "center_y": .5})
        self.dog_card_present = 0
        super(DogBrowseWindow, self).__init__(**kwargs)

    def get_news(self):
        """
        Returns a representation of the most recently added News item as a tuple (title, body).
        """
        news_item = get_all_news(MainApp.db)[-1]
        news_title = news_item[2]
        news_body = news_item[3]
        return (news_title, news_body)

    def update_account(self):
        """
        Updates the current Account. Unsuccessful update if the new email is already registered. Fields that are left blank are unmodified.
        """
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text

        # Update name, if entered
        if name != '':
            update_account_name(MainApp.id_account, name, MainApp.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account name!')
        # Update email, if entered
        if email != '':
            # If email is already registered
            accounts = find_account(email, MainApp.db)
            if len(accounts) > 0:
                # PLACEHOLDER: error message
                print('Error: Failed to update account email. Email is already registered to an account.')
            else:
                update_account_email(MainApp.id_account, email, MainApp.db)
                # PLACEHOLDER: success message
                print('Successfully updated the account email!')
        # Update password, if entered
        if password != '':
            update_account_password(MainApp.id_account, password, MainApp.db)
            # PLACEHOLDER: success message
            print('Successfully updated the account password!')

    def delete_account(self):
        """
        Deletes the current Account.
        """
        # PLACEHOLDER: warning message
        print('Wait! Are you sure you want to delete this account?')

        # PLACEHOLDER: If confirmed yes... delete account
        delete_account(MainApp.id_account, MainApp.db)
        MainApp.id_account = None
        # PLACEHOLDER: success message
        print('Successfully deleted the account!')

    def logout(self):
        """
        Logs out of the current Account.
        """
        MainApp.id_account = None

    def press_change(self):
        self.add_widget(self.change_label)

    def press_delete(self):
        self.add_widget(self.delete_label)

    def clearchange(self):
        if self.change_label:
            self.remove_widget(self.change_label)
    def cleardelete(self):
        if self.delete_label:
            self.remove_widget(self.delete_label)

    def show_dog_profile(self, id_dog):
        self.parent.ids['dog_profile'].set_id(id_dog)
        self.manager.current = "dogprofile"
        self.manager.transition.direction = "left"

    dog_card = ObjectProperty(None)
    dog_card_list = []
    liked_animal_card = ObjectProperty(None)
    liked_animal_card_list = []

    def add_dog(self):
        # Retrieve matching dogs
        dog_search_info = self.parent.ids['dog_search']
        dog_list = get_dogs(dog_search_info.get_breed(), dog_search_info.get_dispositions(), dog_search_info.get_recency(), MainApp.db)
        # PLACEHOLDER: no matching dogs message
        if not dog_list:
            self.add_widget(self.no_results_label)
            self.dog_card_present = 1
        # Add each dog card
        if self.dog_card_present == 0:
            self.dog_card_present = 1
            for dog in dog_list:
                dog_id = dog[0]
                dog_name = dog[1]
                self.dog_card = Button(text=dog_name)
                self.dog_card.bind(on_release = lambda x, id=dog_id: self.show_dog_profile(id))
                self.dog_card_list.append(self.dog_card)
                self.ids.dog_grid.add_widget(self.dog_card)


    def remove_dog(self):
        self.dog_card_present = 0
        self.remove_widget(self.no_results_label)
        for cards in self.dog_card_list:
            self.ids.dog_grid.remove_widget(cards)

    def liked_dog_profile(self):
        self.manager.current = "dogprofile"

    def show_liked_animals(self):
        liked_animal_list = get_liked_animals(MainApp.id_account, MainApp.db)
        for id_animal in liked_animal_list:
            animal = find_animal_by_id(id_animal[0], MainApp.db)[0]
            animal_name = animal[4]
            shelter_name = animal[10]
            self.liked_animal_item = TwoLineAvatarIconListItem(
                IconLeftWidget(
                    icon="information-outline",
                    on_release = lambda x: self.liked_dog_profile()
                ),
                IconRightWidget(
                    icon="minus",
                    on_release=lambda x: self.remove_liked_animal()
                ),
                secondary_text=shelter_name,
                bg_color=(255/255, 233/255, 234/255, 1),
                text_color= (56/255, 45/255, 94/255, 1),
                text=f"[size=54]{animal_name}[/size]"
            )
            self.liked_animal_card_list.append(self.liked_animal_item)
            self.ids.liked_list.add_widget(self.liked_animal_item)

    def remove_liked_animal(self):
        # REMOVED GLOBAL VARIABLE so this will not work anymore
        # print(liked_animal_list)
        print('temporary placeholder')
        # liked_animal_list.remove(self.dog_name)
        # self.ids.liked_list.remove_widget(self.liked_animal_item)

    def reset_liked_list(self):
        if self.liked_animal_card_list:
            for liked_cards in self.liked_animal_card_list:
                self.ids.liked_list.remove_widget(liked_cards)



class DogProfile(Screen):
    id_dog = NumericProperty(None)
    availability = StringProperty('')
    dog_name = StringProperty('')
    birthdate = StringProperty('')
    gender = StringProperty('')
    breed = StringProperty('')
    size_in_lbs = StringProperty('')
    date_created = StringProperty('')
    summary = StringProperty('')

    def __init__(self, **kwargs):
        super(DogProfile, self).__init__(**kwargs)

    def set_id(self, id):
        self.id_dog = id
        self.populate_information()

    def populate_information(self):
        dog_info = find_animal_by_id(self.id_dog, MainApp.db)[0]
        self.availability = dog_info[1]
        self.breed = dog_info[3]
        self.dog_name = dog_info[4]
        self.birthdate = str(dog_info[5])
        self.gender = dog_info[6]
        self.size_in_lbs = str(dog_info[7])
        self.summary = dog_info[8]
        self.date_created = str(dog_info[9])

    def add_liked_animal(self):
        liked_animal_list = get_liked_animals(MainApp.id_account, MainApp.db)
        liked_animal_list = [liked_animal[0] for liked_animal in liked_animal_list]
        if self.id_dog not in liked_animal_list:
            add_liked_animal(MainApp.id_account, self.id_dog, MainApp.db)


class DogSearch(Screen):
    # Store selected breed, disposition(s), and recency
    selected_breed = ''             # breed name
    selected_dispositions = []      # disposition descriptions
    selected_recency = None         # True if most recent, False if least recent
    # Retrieve breeds and dispositions to display
    breeds = [breed[1] for breed in get_dog_breeds(MainApp.db)]
    dispositions = [disposition[1] for disposition in get_dispositions(MainApp.db)]

    def get_breed(self):
        return self.selected_breed

    def get_dispositions(self):
        return self.selected_dispositions

    def get_recency(self):
        return self.selected_recency

    def checkbox_most_recent(self, instance, value):
        """Sets selected_recency to True, indicating the list of displayed dogs is listed in order of most recent"""
        if value == True:
            self.selected_recency = True

    def checkbox_least_recent(self, instance, value):
        """Sets selected_recency to False, indicating the list of displayed dogs is listed in order of most recent"""
        if value == True:
            self.selected_recency = False

    def breed_dropdown(self, value):
        """Sets selected_breed and displays it as the dropdown label's text"""
        self.ids.click_label = value
        self.selected_breed = value


class Dispositions(Button):

    dropdown = ObjectProperty(None)
    values = ListProperty([])               # list of dispositions
    chosen_dispositions = ListProperty([])  # selected dispositions

    def __init__(self, **kwargs):
        self.text="Click here for dispositions"
        self.background_normal= ''
        self.background_color=(0, 187/255, 224/255, 1)
        self.bind(dropdown=self.update_dropdown)
        self.bind(values=self.update_dropdown)
        super(Dispositions, self).__init__(**kwargs)
        self.bind(on_release=self.click_dropdown)

    def click_dropdown(self, *args):
        if self.dropdown.parent:
            self.dropdown.dismiss()
        else:
            self.dropdown.open(self)

    def update_dropdown(self, *args):
        if not self.dropdown:
            self.dropdown = DropDown()
        values = self.values
        if values:
            if self.dropdown.children:
                self.dropdown.clear_widgets()
            for value in values:
                b = Factory.MultiSelectOption(text=value)
                b.bind(state=self.choose_disposition)
                self.dropdown.add_widget(b)

    def choose_disposition(self, instance, value):
        """Sets the selected dispositions in this class (for display as dropdown label's text) and in DogSearch class (for use in search results)."""
        if value == 'down':
            if instance.text not in DogSearch.selected_dispositions:
                self.chosen_dispositions.append(instance.text)
                DogSearch.selected_dispositions.append(instance.text)
        else:
            if instance.text in DogSearch.selected_dispositions:
                self.chosen_dispositions.remove(instance.text)
                DogSearch.selected_dispositions.remove(instance.text)

    def on_chosen_dispositions(self, instance, value):
        """Formats drop label's text."""
        if value:
            self.text = ', '.join(value)
        else:
            self.text = ''

class WindowManager(ScreenManager):
    pass


# --- Main Method --- #
if __name__ == '__main__':
    MainApp().run()