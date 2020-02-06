#!/usr/bin/python3
"""
Write a Python script that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests
import sys
import json
# import pprint

headers = {
    'User-Agent': 'My User Agent 1.0'
}


def number_of_subscribers(subreddit):
    """function that returns the number of subscribers"""
    try:
        url = 'https://www.reddit.com/r/'
        response = requests.get(url + subreddit + "/about.json",
                                headers=headers)
        return response.json()['data']['subscribers']
        # pprint.pprint(SUBREDDIT.json()['data']['subscribers'])
    except:
        return 0
