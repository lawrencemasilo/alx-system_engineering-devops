#!/usr/bin/python3
"""This module uses a REST api for Todo list progress"""
import json
import requests
import sys


def employee_todo_progress():
    """fetches the data"""
    main_url = f"""https://jsonplaceholder.typicode.com/users"""
    todos = f"https://jsonplaceholder.typicode.com/todos"

    employee_response = requests.get(main_url)
    employee_data = employee_response.json()

    exports = {}

    for employee in employee_data:
        employee_id = employee['id']
        name = employee['username']

        todos_response = requests.get(f"{todos}?userId={employee_id}")

        todos_response = requests.get(todos)
        todos_data = todos_response.json()

        for todo in todos_data:
            tasks = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": name
                    }
            exports[employee_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(exports, json_file, indent=4)


if __name__ == "__main__":
    employee_todo_progress()
