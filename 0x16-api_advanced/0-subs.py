#!/usr/bin/python3
"""
a function that queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers) for a
given subreddit.
If an invalid subreddit is given,
the function should return 0.

"""
import requests


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(
            url='{}/r/{}/about.json'.format(
                base_url,
                subreddit
                ),
            headers=headers
            )

        if response.status_code != 200:
            return (0)

        data = response.json()['data']
        subs = data['subscribers']
        return subs

    except Exception:
        return False
