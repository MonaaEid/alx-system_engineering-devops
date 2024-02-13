#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import urllib.request
import json


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as respose:
        html = respose.read()
        data = json.loads(html)
        if respose.status == 200:
            for post in data.get('data').get('children'):
                print(post.get('data').get('title'))
        else:
            print(None)
