#!/usr/bin/python3
""" function that queries the Reddit API and
returns the number of subscribers"""
import requests
import urllib.request
import json


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    try:
        headers = {'User-Agent': 'My Reddit Subscribers Checker'}
        
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, requests.RequestException):
        return 0
