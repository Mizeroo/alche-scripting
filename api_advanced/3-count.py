#!/usr/bin/python3
"""
3-count
"""
import requests


def count_words(subreddit, word_list):
    """Recursively query the Reddit API, parse titles of hot articles,
    and print a sorted count of given keywords.

    Duplicate keywords in word_list are summed (e.g. ['java', 'java']
    counts java matches twice each).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): The list of keywords to count (case-insensitive).

    Returns:
        None
    """
    frequency = {}
    for word in word_list:
        key = word.lower()
        frequency[key] = frequency.get(key, 0) + 1

    totals = {key: 0 for key in frequency}

    _recurse_count(subreddit, frequency, totals)

    filtered = [(word, total) for word, total in totals.items() if total > 0]
    ordered = sorted(filtered, key=lambda item: (-item[1], item[0]))

    for word, total in ordered:
        print("{}: {}".format(word, total))


def _recurse_count(subreddit, frequency, totals, after=None):
    """Recursively walk paginated hot-post results, tallying keyword
    occurrences (weighted by frequency in the original word_list) into
    totals.

    Args:
        subreddit (str): The name of the subreddit to query.
        frequency (dict): Mapping of lowercase keyword to how many times
            it appeared in the original word_list.
        totals (dict): Mapping of lowercase keyword to running count
            (mutated in place).
        after (str): The pagination token for the next page of results.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api.advanced.project:v1.0 (by /u/alche_student)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                             allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    children = data.get("children", [])

    for post in children:
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in totals:
                totals[token] += frequency[token]

    next_after = data.get("after")

    if next_after is not None:
        _recurse_count(subreddit, frequency, totals, next_after)
