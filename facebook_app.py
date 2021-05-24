import json

from kivymd.uix.screen import MDScreen

from components.online_friends import OnlineAvatarImage
from components.posts import Post
from components.story_card import StoryCard


class FacebookApp(MDScreen):
    with open("assets/profile_details.json") as f_obj:
        prof_detail = json.load(f_obj)

    profile_pic = prof_detail["profile_pic"]

    def on_enter(self):
        self.list_online_friends()
        self.list_stories()
        self.list_posts()

    def list_online_friends(self):
        with open("assets/online_friends.json") as f_obj:
            data = json.load(f_obj)
            for friend_name in data:
                self.ids.online_friends.add_widget(OnlineAvatarImage(
                    avatar=data[friend_name]['avatar']
                ))

    def list_stories(self):
        with open("assets/stroies.json") as f_obj:
            data = json.load(f_obj)
            for friend_name in data:
                self.ids.stories.add_widget(StoryCard(
                    name=friend_name,
                    image=data[friend_name]["image"],
                    avatar=data[friend_name]["avatar"]
                ))

    def list_posts(self):
        with open("assets/posts.json") as f_obj:
            data = json.load(f_obj)
            for friend_name in data:
                self.ids.timeline.add_widget(Post(
                    name=friend_name,
                    avatar=data[friend_name]["avatar"],
                    post=data[friend_name]["post"],

                    likes=int(data[friend_name]["likes"]),
                    comments=int(data[friend_name]["comments"]),
                    caption=data[friend_name]["caption"],
                    updated_ago=data[friend_name]["updated_ago"]
                ))
