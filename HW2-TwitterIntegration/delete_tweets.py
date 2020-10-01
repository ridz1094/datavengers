# -*- coding: utf-8 -*-
import tweepy as tw
from  tweet_auth import * 
   
def delete_tweets():
     for status in tw.Cursor(get_api().home_timeline).items(100):
         json = status._json
         get_api().destroy_status(json['id'])



