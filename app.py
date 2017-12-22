# -*- coding: utf-8 -*-

from fbchat import Client
import config


class Martzi(Client):
    """This class interacts with the fbchat API."""

    def onMessage(self, message_object, author_id,
                  thread_id, thread_type, **kwargs):
        print("I got a message!!!")
        self.logout()
        exit()


version = 0.2
print('Welcome to Matrzi v' + str(version))

(username, password) = config.get_credentials()
try:
    client = Martzi(username, password)
    client.listen()
except Exception as e:
        print("Couldn't login to facebook!")
        print(e)
        exit()
