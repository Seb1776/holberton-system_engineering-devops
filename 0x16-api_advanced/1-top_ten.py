#!/usr/bin/python3
"""Get Top 10 Hot Posts"""

import requests


def top_ten(subreddit):
    """Get Top 10 Hot Posts"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    header = {'User-Agent': 'Chrome/66.0.3359.139 Mobile Safari/537.36'}

    params = {"limit": 10}

    response = requests.get(url, headers=header, params=params)

    if response.status_code == 404:
        print('None')
        return

    res = response.json()
    result = res.get('data').get('children')

    for i in result:
        respo = i.get('data').get('title')
        print(respo)
