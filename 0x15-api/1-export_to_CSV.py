#!/usr/bin/python3

"""
export python script to csv
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    param = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(param)
    response_json = requests.get(url, verify=True).json()

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(param)
    todo_json = requests.get(url, verify=True).json()

    with open("USER_ID.csv", 'w', newline='') as file:
        csvreader = csv.writer(file, quoting=csv.QUOTE_ALL)

        for data in todo_json:
            csvreader.writerow([int(param), response_json.get('username'),
                               data.get('completed'), data.get('title')])
