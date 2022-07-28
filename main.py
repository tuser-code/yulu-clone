import kivy
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp
from kivymd.app import MDApp

Window.size = [dp(400),dp(650)]

class YULU(MDApp):
    
    x = Window.size[0]
    y = Window.size[1]

    manager = ScreenManager()

    landing_screen = None

    def build(self):
        return self.manager
    
    def on_start(self):
        self.load_app()

    def load_app(self):
        self.landing_screen = Builder.load_file("screens/land.kv")
        self.manager.add_widget(self.landing_screen)
        self.manager.current = "landing"


YULU().run()

