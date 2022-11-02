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

    all_employees = requests.get(
        "{}/users/".format(
            base_url
        )
    ).json()

    dictionary = {}

    for employee in all_employees:
        username = employee.get('username')
        userId = employee.get('id')
        all_todos = requests.get(
            "{}/todos?userId={}".format(
                base_url,
                userId
            )
            ).json()
        json_task_data = []
        for todo in all_todos:
            json_task_data.append(
                {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get('completed')
                }
            )

        dictionary[str(userId)] = json_task_data

    json_object = json.dumps(dictionary)

    with open("todo_all_employees.json", "w") as jsonfile:
        jsonfile.write(json_object)


if __name__ == "__main__":
    main()
