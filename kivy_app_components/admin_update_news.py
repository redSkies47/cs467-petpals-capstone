from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager



class admin_update_news(Screen):

    # TODO: backend variables for metadata

    def toUpdateNews(self):
        print("Update News")
        #TODO: navigate to admin side - update news page

    def toAddAnimal(self):
        # Builder.load_file('admin_update_news.kv')
        print("Add Animal")
        #TODO: navigate to admin side - add/edit animal page

    def toEditDeleteAnimal(self):
        print("Edit/Delete Animal")
        #TODO: navigate to admin side - delete animal page
