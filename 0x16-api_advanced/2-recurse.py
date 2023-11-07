#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=""):
    """ returns a list containing the titles of all hot articles
    for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    resp = requests.get(url, headers=headers,
                        params={"after": after}, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        after = data['data']['after']
        for post in data['data']['children']:
            hot_list.append(post.get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
