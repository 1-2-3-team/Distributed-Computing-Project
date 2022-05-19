import tweepy
import json
import requests
import datetime
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import time
import subprocess

st = time.time()

client = tweepy.Client(bearer_token='insert bearer token herer')

query = '"cancelled" "racism" OR "racist" ":("'

file_name = 'tweets.json'

with open(file_name, 'a+', encoding="utf-8") as json_file:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['id','text','created_at'], max_results=100).flatten(limit=10000):
        json_file.write('%s\n' % tweet.data)

et = time.time()

ft = et - st

print('Exec time:', ft, 'seconds')

