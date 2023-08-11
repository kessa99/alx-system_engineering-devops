#!/usr/bin/python3

import requests
import json

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'HolbertonSchool/APIUsage'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4)
        print(formatted_data)
    else:
        print("None")

# Utilisation de la fonction
subreddit_name = "python"
top_ten(subreddit_name)

