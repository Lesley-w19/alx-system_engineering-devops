#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.

"""
from sys import argv
import requests
import urllib



def main():
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = argv[1]
    
    all_employees = requests.get(
        "{}/users/{}".format(
            base_url,
            employee_id
        )
    ).json()
    
   
    employee_name = all_employees.get('name')
   
    completed_tasks = 0
    total_tasks = 0
   
    employee_todos = requests.get(
       "{}/users/{}/todos/".format(
           base_url,
           employee_id
        )
    ).json()

    for tasks in employee_todos: 
        total_tasks += 1
        completed = tasks.get('completed')

        if completed == True:
            completed_tasks += 1          

    print("Employee {} is done with tasks({}/{}):\
        ".format(employee_name, completed_tasks, total_tasks))
   
    print('\n'.join(
        ['\t ' + tasks.get('title')
         for tasks in employee_todos
         if tasks.get('completed') == True
         ]
    ))



if __name__ == "__main__":
    main()
   
   
   