#!/usr/bin/python3
"""
Exports data in the CSV format
"""

from requests import get
from sys import argv


if __name__ == '__main__':

    userId = argv[1]
    REST_API = 'https://jsonplaceholder.typicode.com'
    user_url = REST_API + "/users/{}".format(userId)

    todo_url = user_url + "/todos"

    user_record = get(user_url).json()
    username = user_record.get('username')

    todos = get(todo_url).json()

    with open('{}.csv'.format(userId), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(userId, username, todo.get('completed'),
                               todo.get('title')))
