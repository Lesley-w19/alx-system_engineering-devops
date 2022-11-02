#!/usr/bin/python3
"""
a function that queries the Reddit API
and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    base_url = 'https://api.reddit.com'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 10
    }

    try:
        response = requests.get(
            url='{}/r/{}/hot.json'.format(
                base_url,
                subreddit
                ),
            params=params,
            headers=headers
        )

        if response.status_code != 200:
            print(None)
            return

        children_data = response.json()['data']['children']

        if len(children_data) == 0:
            print(None)
            return
        else:
            for posts in children_data:
                title = posts['data']['title']
                print(title)

    except Exception:
        return False
