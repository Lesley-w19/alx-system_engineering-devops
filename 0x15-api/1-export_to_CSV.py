#!/usr/bin/python3
"""
what you did in the task #0, extend your
Python script to export data in the CSV format.
"""


import csv
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
    ).json().get('name')

    with open('{}.csv'.format(employee_id), 'w') as csvfile:
        my_writer = csv.writer(
            csvfile, delimiter=",",
            quotechar='"', quoting=csv.QUOTE_ALL,
            lineterminator="\n"
        )

        for data in employee_todos:
            id = data.get('userId')
            status = data.get("completed")
            title = data.get('title')

            my_writer.writerow(
                [
                    id, employee_name,
                    status, title
                ]
            )


if __name__ == "__main__":
    main()
