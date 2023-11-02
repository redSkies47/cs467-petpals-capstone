import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.label import Label
# from kivy.core.window import Window
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen



class LoginScreen(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file('../kv_design_language/user_front.kv')

class LoginWindow(Screen):
    pass

class CreateAccountWindow(Screen):
    pass

class LandingWindow(Screen):
    def __init__(self, **kwargs):
        super(LandingWindow, self).__init__(**kwargs)
        self.change_label = Label(text="Changes Submitted!",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
        self.delete_label = Label(text="Account Deleted.",
                              color = (255/255, 0/255, 0/255, 1),
                              font_size = 25,
                              pos_hint = {"center_x": 0.5, "center_y": .95})
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

class WindowManager(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return Builder.load_file('../kv_design_language/user_front.kv')

if __name__ == '__main__':
    LoginScreen().run()