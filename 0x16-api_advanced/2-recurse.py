#!/usr/bin/python3
""" import"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[], alfer=None):
    """Use the recursive function"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'HolbertonSchool/APIUsage'}
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)

    if r.status_code == 200:
        data = r.json()
        list_title = data['data']['children']

        if list_title:
            for post in list_title:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return (None)
