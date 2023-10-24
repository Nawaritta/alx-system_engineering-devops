#!/usr/bin/python3
"""
Exports data in the JSON format.
"""

from json import dump
from requests import get
from sys import argv

if __name__ == '__main__':

    REST_API = 'https://jsonplaceholder.typicode.com'
    users_url = REST_API + "/users/"
    all_users = get(users_url).json()

    for user in all_users:

        userId = user.get('id')
        username = user.get('username')
        todos_url = users_url + "{}".format(userId) + "/todos"
        todos = get(todos_url).json()

        todos_data = []

        for todo in todos:
            todo_data = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": username
            }
            todos_data.append(todo_data)

            with open('todo_all_employees.json', 'w') as f:
                dump({userId: todos_data}, f)
