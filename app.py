# -*- coding: utf-8 -*-

from fbchat import Client
import random
import re
import config
import requests


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
        print("I recieved command:", cmd)
        self.execute_command(cmd)

    def send_random_reddit_thread(self, subreddit):
        url = 'https://www.reddit.com/r/' + subreddit + '/.json'
        headers = {'User-agent': 'Matrzi v' + str(VERSION)}
        r = requests.get(url, headers=headers)
        print(r.json())


    def execute_command(self, cmd):
        if cmd in subreddit.keys():
            # Select a random subreddit
            sub = subreddit[cmd][random.randint(0, len(subreddit[cmd]) - 1)]
            self.send_random_reddit_thread(sub)


def login():
    try:
        print("Logging in...")
        client = Martzi(username, password, logging_level=30)
        print("Logged in successfully!")
        print("Listening...")
        # client.listen()
        client.send_random_reddit_thread('PrequelMemes')
        input()
    except Exception as e:
        print("Couldn't login to facebook!")
        print(e)
        exit()


VERSION = 0.2
print('Welcome to Matrzi v' + str(VERSION))

(username, password) = config.get_credentials()
subreddit = config.parse_file('subreddits.txt')
login()
