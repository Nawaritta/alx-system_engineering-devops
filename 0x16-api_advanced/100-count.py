#!/usr/bin/python3
"""
This module defines a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces. Javascript should count
as javascript, but java should not).
"""
import requests
import sys


def recurse(subreddit, dictionary, after=None):
    """ Collects info on the hot posts from a given subreddit, and counts
    the occurrences of specific words from a provided word list"""

    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers,
                            params={'after': after}, allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json()
    hot_posts = data.get('data', {}).get('children', [])

    for post in hot_posts:
        title = post.get('data', {}).get('title', '').lower().split()
        for word in title:
            word = word.strip('.,!_')
            if word in dictionary:
                dictionary[word] += 1

    after = data.get('data', {}).get('after')
    if not after:
        return
    return recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """prints a sorted count of given keywords"""

    word_dict = {word.lower(): 0 for word in word_list}

    recurse(subreddit, word_dict)

    sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        if count != 0:
            print('{}: {}'.format(word, count))
        else:
            print('')
