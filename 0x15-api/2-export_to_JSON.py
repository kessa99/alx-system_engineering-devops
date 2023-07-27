#!/usr/bin/python3

"""
extends to Json format
1- enter
2- connexion to obtain information of user (first url)
3- json format obtain(response_json)
4- todo list obtain (second url)
5- obtain todo list in format json
{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
"""

import json
import requests
import sys

if __name__ == "__main__":
    param = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(param)
    response_json = requests.get(url, verify=True).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(param)
    todo_json = requests.get(url, verify=True).json()
    user_id = "{}".format(param)

    user_info = {
        user_id: []
    }

    for task in todo_json:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": response_json.get("username")
        }
        user_info[user_id].append(task_info)

    with open("{}.json".format(param), 'w') as file:
        json.dump(user_info, file)
