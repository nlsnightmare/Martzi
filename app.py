from fbchat import Client
import getpass


class Martzi(Client):
    """This class interacts with the fbchat API."""

    def onMessage(self, message_object, author_id,
                  thread_id, thread_type, **kwargs):
        print("I got a message!!!")


version = 0.1
print('Welcome to Matrzi v' + str(version))
# TODO: maybe read username & password from config file?
username = input('Username: ')
password = getpass.getpass(prompt='Password: ', stream=None)
try:
    client = Martzi(username, password)
except Exception:
        print("Couldn't login to facebook!")
        exit()

client.logout()
