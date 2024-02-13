#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list 
containing the titles of all hot articles for a given subreddit."""

import urllib.request
import json


def recurse(subreddit, hot_list=[]):
    """comment"""
    