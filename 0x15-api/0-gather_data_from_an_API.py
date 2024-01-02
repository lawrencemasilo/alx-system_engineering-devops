#!/usr/bin/python3
"""This module uses a REST api for Todo list progress"""
import requests
import sys


def employee_todo_progress(employee_id):
    """fetches the data"""
    main_url = f"""https://jsonplaceholder.typicode.com/users/{employee_id}"""
    todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_response = requests.get(main_url)
    employee_data = employee_response.json()
    name = employee_data.get('name')

    todos_response = requests.get(todos)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    tasks = [task for task in todos_data if task['completed']]

    print(f"Employee {name} is done with tasks({len(tasks)}/{total_tasks}):")

    for task in tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    employee_todo_progress(int(sys.argv[1]))
