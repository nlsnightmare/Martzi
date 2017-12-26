# -*- coding: utf-8 -*-

from fbchat import Client
import random
import re
import config
import requests
import reddit


class Martzi(Client):
    """This class interacts with the fbchat API."""

    def onMessage(self, message_object, author_id,
                  thread_id, thread_type, **kwargs):
        msg = message_object.text
        if author_id == self.uid or (not msg.startswith('!')):
            return  # Ignore your messages
        pattern = re.compile('!(.*) ?.*')
        m = pattern.match(msg)
        cmd = m.groups(0)[0]
        ans = self.execute_command(cmd, author_id)

        self.sendMessage(ans, thread_id=thread_id, thread_type=thread_type)

    def execute_command(self, cmd, sender):
        if cmd in subreddit.keys():
            # Select a random subreddit
            sub = subreddit[cmd][random.randint(0, len(subreddit[cmd]) - 1)]
            (perma, url, text) = reddit.send_random_reddit_thread(sub)
            if not url == '':
                return url
            elif not text == '':
                return text
            else:
                return perma
        elif cmd == 'die':
            if sender in config.mods:
                # TODO: Maybe send a dying message?
                exit()
            # TODO: Add customized message
            msg = self.get_username(sender) + " can't kill me!"
            return msg

    def get_username(self, user_id):
        user = self.fetchUserInfo(user_id)[user_id]
        return user.name


def login():
    try:
        print("Logging in...")
        client = Martzi(username, password, logging_level=30)
        print("Logged in successfully!")
        print("Listening...")
        client.listen()
    except Exception as e:
        print("Couldn't login to facebook!")
        print(e)
        exit()


VERSION = 0.2
print('Welcome to Matrzi v' + str(VERSION))

(username, password) = config.get_credentials()
subreddit = config.parse_file('subreddits.txt')
login()
