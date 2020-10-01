# -*- coding: utf-8 -*-
import tweepy as tw
from  tweet_auth import * 

def display_tweets():
    for status in tw.Cursor(get_api().home_timeline).items(100):
        status_json = status._json
        print(status_json['text'])



