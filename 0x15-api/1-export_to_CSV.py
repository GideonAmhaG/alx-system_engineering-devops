#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
 data in the CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    _id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": _id}).json()
    with open("{}.csv".format(_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [_id, username, a.get("completed"), a.get("title")])
            for a in todos]
