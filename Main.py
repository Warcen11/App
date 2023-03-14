from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
import botMenu 

Config.set('kivy', 'default_font', 'Arial')

class MyApp(App):
    def build(self):
        app=BoxLayout(orientation='vertical')
        main=BoxLayout(orientation='vertical')
        main.add_widget(Button())
        app.add_widget(TextInput(size_hint_y=None, height=60, font_size = 32))
        app.add_widget(main)
        app.add_widget(botMenu.botMenu)
        return app
if __name__=="__main__":
    MyApp().run()