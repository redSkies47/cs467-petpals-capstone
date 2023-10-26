from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
Builder.load_file('createacc.kv')
email = ObjectProperty(None)
password = ObjectProperty(None)

class MyGridLayout(Widget):
    # def __init__(self, **kwargs):
    #     super(MyGridLayout, self).__init__(**kwargs)

    #     self.cols = 1
    #     self.top_grid = GridLayout()
    #     self.top_grid.cols = 2

    #     self.top_grid.add_widget(Label(text="Email: "))
    #     self.email = TextInput(multiline=False)
    #     self.top_grid.add_widget(self.email)

    #     self.top_grid.add_widget(Label(text="Password: "))
    #     self.password = TextInput(multiline=False)
    #     self.top_grid.add_widget(self.password)

    #     self.add_widget(self.top_grid)

    #     self.login = Button(text="Login", 
    #         font_size=30,
    #         size_hint_y = None,
    #         height = 75)
    #     self.login.bind(on_press=self.presslog)
    #     self.add_widget(self.login)

    #     self.account = Button(text="Create Account", 
    #         font_size=30,
    #         size_hint_y = None,
    #         height = 75)
    #     self.account.bind(on_press=self.pressacc)
    #     self.add_widget(self.account)

    def presslog(self):
        self.add_widget(Label(text="Login Successful"))
    
    def pressacc(self):
        self.add_widget(Label(text="One moment please"))

class MainApp(App):

    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MainApp().run()