#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively query the Reddit API and return a list of titles of
    all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The accumulated list of titles (used internally
            for recursion). Do not pass this manually.
        after (str): The pagination token for the next page of results
            (used internally for recursion).

    Returns:
        list: A list of all hot post titles, or None if the subreddit
            is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api.advanced.project:v1.0 (by /u/alche_student)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                             allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return None

    children = data.get("children", [])

    if not children and not hot_list:
        return None

    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    next_after = data.get("after")

    if next_after is None:
        return hot_list

    return recurse(subreddit, hot_list, next_after)
