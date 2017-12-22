# -*- coding: utf-8 -*-

from fbchat import Client
import config


class Martzi(Client):
    """This class interacts with the fbchat API."""

    def onMessage(self, message_object, author_id,
                  thread_id, thread_type, **kwargs):
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id,
                      thread_type=thread_type)


def login():
    try:
        print("Logging in...")
        client = Martzi(username, password, logging_level=50)
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
