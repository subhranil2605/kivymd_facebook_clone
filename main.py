from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

from facebook_app import FacebookApp

Window.size = (300, 600)


class App(MDApp):
    def build(self):
        self.load_kv_files()
        return FacebookApp()

    def load_kv_files(self):
        Builder.load_file('facebook_app.kv')
        Builder.load_file('components/top_three_buttons.kv')
        Builder.load_file('components/avatar_image.kv')
        Builder.load_file('components/online_friends.kv')
        Builder.load_file('components/story_card.kv')
        Builder.load_file("components/posts.kv")

    def on_start(self):
        self.root.dispatch("on_enter")


App().run()
