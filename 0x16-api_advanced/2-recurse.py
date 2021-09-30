#!/usr/bin/python3
"""Recursion"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursion"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    header = {'User-Agent': 'Chrome/66.0.3359.139 Mobile Safari/537.36'}

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=header, params=params)

    if response.status_code == 404:
        return None

    results = response.json().get("data")

    after = results.get("after")
    count += results.get("dist")

    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
