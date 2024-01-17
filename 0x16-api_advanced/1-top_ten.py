#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    response = requests.get(
            url,
            headers={"User-Agent": "linux:0x16.api.advanced:v1.0.0"},
            params={"limit": 10},
            allow_redirects=False
            )
    if response.status_code == 404:
        print("None")
        return
    else:
        data = response.json().get("data")
        children = data.get("children")
        for post in children:
            title = post.get("data").get("title")
            print(title)
