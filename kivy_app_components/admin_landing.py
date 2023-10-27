from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from admin_update_news import AdminUpdateNewsScreen

class MainApp(MDApp):

    def build(self):
        Window.size = (295, 620)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        # Builder.load_file('admin_update_news.kv')
        return Builder.load_file('admin_landing.kv')
    
class AdminLandingScreen(Screen):

    #TODO: backend variables for metadata

    def toUpdateNews(self):
        print("Update News")
        #TODO: navigate to admin side - update news page

    def toAddEditAnimal(self):
        print("Add/Edit Animal")
        #TODO: navigate to admin side - add/edit animal page

    def toDeleteAnimal(self):
        print("Delete Animal")
        #TODO: navigate to admin side - delete animal page

if __name__ == '__main__':
    MainApp().run()