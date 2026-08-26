# API advanced

Python scripts for querying the Reddit API: subscriber counts, hot post
titles (with pagination via recursion), and keyword frequency counting
across all hot posts in a subreddit.

## Files

- `0-subs.py` — `number_of_subscribers(subreddit)`
- `1-top_ten.py` — `top_ten(subreddit)`
- `2-recurse.py` — `recurse(subreddit, hot_list=None, after=None)`
- `3-count.py` — `count_words(subreddit, word_list)`

## Notes

- No OAuth is required for these read-only endpoints, but a custom
  `User-Agent` header is required or Reddit will rate-limit/reject
  requests.
- Invalid subreddits redirect (302) to a search page rather than
  returning 404, so all requests are made with `allow_redirects=False`
  and a non-200 status is treated as invalid.
