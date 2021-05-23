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
        with open(r"E:\KIvyMD_Facebook\assets\online_friends.json") as f_obj:
            data = json.load(f_obj)

            for friends in data:
                name = friends
                avatar = data[friends]['avatar']
                print(name, avatar)
                self.ids.online_friends.add_widget(OnlineAvatarImage(
                    avatar=avatar
                ))

    def list_stories(self):
        with open("assets/stroies.json") as f_obj:
            data = json.load(f_obj)
            for d in data:
                self.ids.stories.add_widget(StoryCard(
                    name=d,
                    image=data[d]["image"],
                    avatar=data[d]["avatar"]
                ))

    def list_posts(self):
        with open("assets/posts.json") as f_obj:
            data = json.load(f_obj)
            for d in data:
                self.ids.timeline.add_widget(Post(
                    name=d,
                    avatar=data[d]["avatar"],
                    post=data[d]["post"],

                    likes=int(data[d]["likes"]),
                    comments=int(data[d]["comments"]),
                    caption=data[d]["caption"],
                    updated_ago=data[d]["updated_ago"]
                ))