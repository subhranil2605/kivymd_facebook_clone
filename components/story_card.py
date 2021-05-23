from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout


class StoryCard(MDRelativeLayout):
    name = StringProperty()
    avatar = StringProperty()
    image = StringProperty()