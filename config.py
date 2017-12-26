import re
import getpass

configfile = 'config.dat'
configdata = []
preferences = {}
mods = []


def cleanup_data(data):
    newdata = []
    for i in range(0, len(data)):
        # Trim endline chars and remove empty lines
        if data[i].endswith('\n') and data[i] != '\n':
            newdata.append(data[i][:-1])
    return newdata


def get_credentials():
    if 'username' in preferences.keys() and 'password' in preferences.keys():
        return (preferences['username'], preferences['password'])
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
    return (username, password)


def parse_file(filename):
    """Parses a data file and returns a dict"""

    answers = {}
    f = open(filename, 'r')
    lines = f.readlines()
    pattern = re.compile(': *\n')
    for l in lines:
        # if l.endswith(':\n'):
        if not pattern.search(l) is None:
            question = re.sub(': *\\n', '', l)
            answers[question] = []
            continue
        ans = l.strip()
        answers[question].append(ans)
    return answers


def parse_config():
    pattern = re.compile('(.*): ?(.*)')
    args = re.compile(', *')
    for l in configdata:
        m = pattern.match(l)
        (setting, parameters) = m.groups()
        t = args.split(parameters)
        if len(t) == 1:
            parameters = t[0]
        else:
            parameters = t

        preferences[setting] = parameters


try:
    f = open('config.dat', 'r')
    configdata = f.readlines()
    configdata = cleanup_data(configdata)
    f.close()
except FileNotFoundError:
    print("No config file found!")
    exit()
parse_config()
