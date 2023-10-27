from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from admin_update_news import admin_update_news

class admin_landing(MDApp):

    def build(self):
        Window.size = (295, 620)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file('admin_landing.kv')
    
    def toUpdateNews(self):
        print("Update News")
        #TODO: navigate to admin side - update news page

    def toAddAnimal(self):
        print("Add Animal")
        #TODO: navigate to admin side - add/edit animal page

    def toEditDeleteAnimal(self):
        print("Edit/Delete Animal")
        #TODO: navigate to admin side - delete animal page


if __name__ == '__main__':
    admin_landing().run()