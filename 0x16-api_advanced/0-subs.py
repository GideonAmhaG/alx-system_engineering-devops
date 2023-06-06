#!/usr/bin/python3
"""module for the function below"""
import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the number of
 subscribers (not active users, total subscribers) for a given subreddit.
 If an invalid subreddit is given, the function should return 0."""
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-agent": "custom"})
    if(r.status_code == 200):
        return r.json().get("data").get("subscribers")
    return 0
