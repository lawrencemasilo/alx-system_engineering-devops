#!/usr/bin/python3
"""This module uses a REST api for Todo list progress"""
import json
import requests
import sys


def employee_todo_progress(employee_id):
    """fetches the data"""
    main_url = f"""https://jsonplaceholder.typicode.com/users/{employee_id}"""
    todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_response = requests.get(main_url)
    employee_data = employee_response.json()
    name = employee_data.get('username')

    todos_response = requests.get(todos)
    todos_data = todos_response.json()
    exports = {employee_id: []}

    for todo in todos_data:
        tasks = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": name
                }
        exports[employee_id].append(tasks)

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(exports, json_file, indent=4)


if __name__ == "__main__":
    employee_todo_progress(int(sys.argv[1]))
