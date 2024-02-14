#!/usr/bin/python3
""" function that queries the Reddit API and
returns the number of subscribers"""

import urllib.request
import json


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as respose:
        html = respose.read()
        data = json.loads(html)
        return data.get('data').get('subscribers', 0)
