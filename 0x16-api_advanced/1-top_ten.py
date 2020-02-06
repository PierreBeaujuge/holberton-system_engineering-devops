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


def top_ten(subreddit):
    """function that returns the titles of the first 10 hot posts"""
    try:
        url = 'https://www.reddit.com/r/'
        response = requests.get(url + subreddit + "/hot.json?limit=10",
                                headers=headers)
        myArray = [element['data']['title'] for element in response.
                   json()['data']['children']]
        print(*myArray, sep='\n')
        # pprint.pprint(response.json())
    except:
        print(None)
