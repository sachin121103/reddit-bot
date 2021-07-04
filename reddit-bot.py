#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:50:52 2021

@author: sachinprabhuram
"""

import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="5b2US_IwjRjvbg",
    client_secret="_FUG-LERHo7g5BgljlMcjV4AmMgzXA",
    user_agent="<console: MyNews: 1.0",
    )


def print_content():
    
    posts = []
    subreddit_name = input("Input a subreddit name: ")
    subreddit_naming = reddit.subreddit(subreddit_name)
    
    for post in subreddit_naming.hot(limit=10):
        posts.append([post.title, post.score, post.url, post.selftext])
    
    posts = pd.DataFrame(posts,columns=['title', 'score','url', 'body'])
    posts.to_csv(r'/Users/sachinprabhuram/Desktop/news.csv', index = False)
    print(posts)
        
print_content()

