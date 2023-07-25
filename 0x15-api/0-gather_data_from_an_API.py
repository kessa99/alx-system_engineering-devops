#!/usr/bin/python3
"""Script python with API Rest to import information"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        rpse = requests.get("{}users/{}".format(url, user))
        name = rpse.json().get("name")

        if name is not None:
            scd_rpse =
            requests.get("{}todo?userId={}".format(url, user)).json()
            all_task = len(scd_rpse)
            done_task = []

            for task in scd_rpse:
                if task.get("completed") is True:
                    done_task.append(task)
            count = len(done_task)
            print("Employee {} is done with tasks({}/{}): ".format(name, count, done_task))
            for title in done_task:
                print("\t {}".format(title.get("title")))
