#!/usr/bin/python3
"""
Uses a REST API to return information about TODO list progress of a user.
"""

from requests import get
from sys import argv

if __name__ == '__main__':

    REST_API = 'https://jsonplaceholder.typicode.com'
    user_url = REST_API + "/users/{}".format(argv[1])
    todos_url = user_url + "/todos"


    user_record = get(user_url).json()
    todos = get(todos_url).json()
    todos_done = [todo for todo in todos if todo.get("completed")]

    username = user_record.get("name")

    print("Employee {} is done with tasks({}/{}):"
          .format(username, len(todos_done), len(todos)))
    for todo in todos_done:
        print("\t{}".format(todo.get("title")))
