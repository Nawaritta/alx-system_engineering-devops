#!/usr/bin/python3
"""
Exports data in the CSV format
"""

from requests import get
from sys import argv


if __name__ == '__main__':

    userId = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + userId
    todo_url = user_url + "/todos"

    user_record = get(user_url)
    username = user_record.json().get('username')

    todos = get(todo_url).json()

    with open('{}.csv'.format(userId), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(userId, username, todo.get('completed'),
                               todo.get('title')))
