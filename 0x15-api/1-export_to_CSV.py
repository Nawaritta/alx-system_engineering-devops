#!/usr/bin/python3
"""
Exports data in the CSV format
"""
from requests import get
from sys import argv

if __name__ == '__main':

    userId = argv[1]
    REST_API = 'https://jsonplaceholder.typicode.com'
    user_url = REST_API + "/users/{}".format(userId)
    todos_url = user_url + "/todos"

    user_record = get(user_url).json()
    todos = get(todos_url).json()
    username = user_record.get("username")


    with open('{}.csv'.format(userId), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'.format(
                userId, username, todo.get('completed'), todo.get('title')))
