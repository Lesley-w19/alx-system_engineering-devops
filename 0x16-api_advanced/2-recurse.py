#!/usr/bin/python3
"""
a recursive function that queries the
Reddit API and returns a list containing
the titles of all hot articles for a given
subreddit. If no results are found for the
given subreddit, the function should return None
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    base_url = 'https://api.reddit.com'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'after': after
    }

    try:
        if after is None:
            return

        response = requests.get(
            url='{}/r/{}/hot.json'.format(
                base_url,
                subreddit
            ),
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            return None

        res = response.json()['data']
        after = res['after']

        children_data = response.json()['data']['children']

        if len(children_data) == 0:
            return None
        else:
            for post in children_data:

                hot_list.append(post['data']['title'])

            recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return False
