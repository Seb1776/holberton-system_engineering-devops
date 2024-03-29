#!/usr/bin/python3
'''URL API from JSON bait'''

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + 'users/{}'.format(int(argv[1]))).json()
    all = requests.get(url + 'todos?userId={}'.format(int(argv[1]))).json()

    response = []

    for task in all:
        if task.get('completed') is True:
            response.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.
          format(user.get('name'), len(response), len(all)))

    for task in response:
        print('\t {}'.format(task))
