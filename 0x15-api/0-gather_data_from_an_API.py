#!/usr/bin/python3

"""
Script python with API Rest to import information.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    """
    Step1 Connection to API
    """
    if len(argv) > 1:
        user = int(argv[1])
        url = "https://jsonplaceholder.typicode.com/"
        response_API = requests.get("{}users/{}".format(url, user))
        """
        Check if the status code is 200
        """
        if response_API.status_code == 200:
            """
                Obtain response_API in json format
            """
            data = response_API.text
            json_format = json.loads(data)
            name = json_format.get("name")

            if name is not None:
                """
                check if name variable is not empty
                """
                second_rpse = requests.get("{}todos?userId={}"
                                           .format(url, user))
                data1 = second_rpse.text
                second_json_format = json.loads(data1)
                all_task = len(second_json_format)
                done_task = []

            for task in second_json_format:
                if task.get("completed") is True:
                    done_task.append(task)
            count = len(done_task)
            print("Employee {} is done with tasks({}/{}): ".format(name,
                  count, all_task))
            for title in done_task:
                print("\t {}".format(title.get("title")))
