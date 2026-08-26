#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """Query the Reddit API and print the titles of the first 10 hot
    posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api.advanced.project:v1.0 (by /u/alche_student)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                             allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
