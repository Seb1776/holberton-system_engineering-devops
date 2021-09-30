#!/usr/bin/python3
"""Get subs from reddit"""

import requests


def number_of_subscribers(subreddit):
    """Get subs from reddit"""

    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)

    header = {
        'User-Agent':  'Chrome/66.0.3359.139 Mobile Safari/537.36'
    }

    response = requests.get(url, headers=header)

    if response.status_code == 404:
        return 0

    res = response.json().get('data')
    return res.get('subscribers')
