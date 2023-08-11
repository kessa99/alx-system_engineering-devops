#!/usr/bin/python3
""" Export """
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """read reddit API and return subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'HolbertonSchool/APIUsage'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        sub = data['data']['subscribers']
        return sub
    else:
        return 0
