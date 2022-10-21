#!/usr/bin/python3
"""
what you did in the task #0, extend your
Python script to export data in the CSV format.
"""


import csv
import json
import requests
from sys import argv


def main():
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = argv[1]

    employee_todos = requests.get(
        "{}/users/{}/todos/".format(
            base_url,
            employee_id
        )
    ).json()

    employee_name = requests.get(
        "{}/users/{}".format(
            base_url,
            employee_id
        )
    ).json().get('username')

    json_task_data = []
    dictionary = {}

    for data in employee_todos:
        json_task_data.append(
            {
                "task": data.get("title"),
                "completed": data.get("completed"),
                "username": employee_name,
            }
        )

    dictionary[employee_id] = json_task_data
    json_object = json.dumps(dictionary)

    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        jsonfile.write(json_object)


if __name__ == "__main__":
    main()
