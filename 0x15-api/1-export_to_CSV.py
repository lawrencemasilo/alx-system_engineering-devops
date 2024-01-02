#!/usr/bin/python3
"""This module uses a REST api for Todo list progress"""
import csv
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
    total_tasks = len(todos_data)
    tasks = [task for task in todos_data if task['completed']]
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            w.writerow(
                    [
                        employee_id, name,
                        todo.get("completed"),
                        todo.get("title")
                        ]
                    )


if __name__ == "__main__":
    employee_todo_progress(int(sys.argv[1]))
