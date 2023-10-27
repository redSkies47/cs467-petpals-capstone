from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager



class admin_update_news(Screen):

    # TODO: backend variables for metadata

    def toButton1(self):
        print("button 1")
        #TODO: navigate to admin side - update news page

    def toButton2(self):
        # Builder.load_file('admin_update_news.kv')
        print("button 2")
        #TODO: navigate to admin side - add/edit animal page

    def toButton3(self):
        print("button 3")
        #TODO: navigate to admin side - delete animal page
