import re
import getpass

configfile = 'config.dat'
configdata = []

try:
    f = open('config.dat', 'r')
    configdata = f.readlines()
    f.close()
except FileNotFoundError:
    print("No config file found!")
    exit()


def get_credentials():
    lines = len(configdata)
    l1 = configdata[0] if lines > 0 else ''
    l2 = configdata[1] if lines > 1 else ''
    username = ''
    password = ''
    if (not l1.startswith('username')) or (not l2.startswith('password:')):
        username = input('Username: ')
        password = getpass.getpass(prompt='Password: ', stream=None)

        save = input("Would you like to save you login credentials?(Y/n) ")
        if save == 'Y' or save == 'y' or save == '':
            # Save login credentials
            with open(configfile, 'r') as original:
                data = original.read()
            with open(configfile, 'w') as modified:
                modified.write('username: ' + username + '\n' +
                               'password: ' + password + '\n' +
                               data)
                print("Saved!")

    else:
        username = re.sub('username: ?', '', l1)
        password = re.sub('password: ?', '', l2)
    return (username, password)
