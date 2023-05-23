#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
 data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    _id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": _id}).json()
    with open("{}.json".format(_id), "w", newline="") as jsonfile:
        json.dump({_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username}
            for todo in todos]}, jsonfile)
