#!/usr/bin/python3
""" function that queries the Reddit API and
returns the number of subscribers"""

import urllib.request
import json


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = urllib.request.Request(url, headers=headers, allow_redirects=False)
    with urllib.request.urlopen(request) as response:
        html = response.read()
        data = json.loads(html)
        if response.status == 200:
            return data.get('data').get('subscribers')
        else:
            return 0
