#!/usr/bin/python3
"""module for the function below"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """a recursive function that queries the Reddit API and returns a list
 containing the titles of all hot articles for a given subreddit. If no
 results are found for the given subreddit, the function should return None"""
    r = requests.get("https://reddit.com/r/{}/hot.json?after={}".
                     format(subreddit, after),
                     headers={"User-agent": "custom"})
    if r.status_code != 200:
        return None
    if after is None:
        return hot_list
    for i in r.json().get("data").get("children"):
        hot_list.append(i.get("data").get("title"))
    after = r.json().get("data").get("after")
    return recurse(subreddit, hot_list, after)
