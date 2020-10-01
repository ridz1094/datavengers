# -*- coding: utf-8 -*-

import tweepy as tw
from  tweet_auth import * 
        
def post_tweet():
    print("Posting tweet on twitter")
    get_api().update_status("Tweepy test")
    
