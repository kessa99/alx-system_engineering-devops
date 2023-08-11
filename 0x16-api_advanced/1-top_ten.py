#!/usr/bin/python3
"""import"""
import json
import requests
import sys


def top_ten(subreddit):
    """ print the first 10 hot post"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'HolbertonSchool/APIUsage'}
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()['data']['children']
        for a in data[:10]:
            print(a['data']['title'])
    else:
        return print(None)
