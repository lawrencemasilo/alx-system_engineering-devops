#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    res = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json"
            )
    if res.status_code == 200:
        data = res.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else:
        return 0
