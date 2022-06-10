#!/usr/bin/env python3

'''
galvan_luis@gmail.com

Copyright (C) 2022 by Luis Yovanny Bedolla Galvan 

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without l> imitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF 
ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT 
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR 
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.

'''

import os
import tweepy
from datetime import datetime
from datetime import date
import json

#Create a json file 
json_data = []

#Twitter authentication bearer token
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAANuxcgEAAAAAeitc4HhcF6x8fa4rXraHDUfHHxk%3D0tMQAlTmuPIKoR3ozJH7gHaKVfV43Z8oqPFb6iVNV3LMPWiVG9")
#auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAANuxcgEAAAAAeitc4HhcF6x8fa4rXraHDUfHHxk%3D0tMQAlTmuPIKoR3ozJH7gHaKVfV43Z8oqPFb6iVNV3LMPWiVG9")
#api = tweepy.API(auth)

#Twitter query
#date_since = "2019-01-01"
#date_until = date.today()

queryTopic = '"cancel culture" OR "#cancelculture" "-filter:retweets" "-filter:safe" :('
#for tweet in tweepy.Cursor(api.search_tweets, q=queryTopic, lang='en', tweet_fields=['id','text','created_at'], result_type = "recent", count=100).items(10):
#    json_data.append(tweet._json)

#json_data.append(tweets.json)
with open('tweets.json', 'a+', encoding = "utf-8") as json_file:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=queryTopic,
                                  tweet_fields=['id','text','created_at'], max_results=100).flatten(limit=1000):
        json.dump(json_data, ensure_ascii=True, indent=4, sort_keys=True, fp=json_file)



json_file.write





