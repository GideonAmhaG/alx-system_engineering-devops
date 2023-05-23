#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
 information about his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    name = user.get("name")
    completed = [a.get("title") for a in todos if a.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), len(todos)))
    [print("\t {}".format(e)) for e in completed]
