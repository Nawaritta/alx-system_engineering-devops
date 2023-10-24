#!/usr/bin/python3
"""
Exports data in the JSON format.
"""

from json import dump
from requests import get
from sys import argv

if __name__ == '__main__':

    userId = argv[1]
    REST_API = 'https://jsonplaceholder.typicode.com'
    user_url = REST_API + "/users/{}".format(userId)
    todos_url = user_url + "/todos"

    user_record = get(user_url)
    username = user_record.json().get('username')
    todos = get(todos_url).json()

    todos_data = []
    for todo in todos:
        todo_data = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        todos_data.append(todo_data)

    with open('{}.json'.format(userId), 'w') as f:
        dump(todos_data, f)
