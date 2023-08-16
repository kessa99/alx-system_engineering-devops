#!/usr/bin/python3

"""
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
            "username": task.get("username"),
            "task": task.get("task"),
            "completed": task.get("completed")
        }

    user_info[user_id].append(task_info)

    with open("{}.json".format(param), 'w') as file:
        json.dump(user_info, file)
