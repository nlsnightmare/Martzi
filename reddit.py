import requests
import random


def send_random_reddit_thread(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'User-agent': 'Matrzi'}
    r = requests.get(url, headers=headers)
    json = r.json()
    data = json['data']['children']
    num_threads = len(data)
    rand = random.randint(0, num_threads - 1)
    thread = data[rand]
    print(thread)
    input()

send_random_reddit_thread('ProgrammerHumor')
