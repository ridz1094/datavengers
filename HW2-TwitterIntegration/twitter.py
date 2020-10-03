# -*- coding: utf-8 -*-
from  tweet_auth import * 
        
def post_tweet(message):
  print("Posting tweet on twitter!!")
  get_api().update_status(message)
   
def delete_tweet(id):
  get_api().destroy_status(id)

def display_tweets():
  tweets = []
  for status in tw.Cursor(get_api().home_timeline).items():
    status_json = status._json
    tweets.append({"id": status_json.get('id'), "status": status_json.get('text'), "created_at": status_json.get('created_at')})
  return tweets

def search_tweet(search_string):
  tweets = []
  for obj in get_api().search(search_string):
    obj_json = obj._json
    tweets.append({"id": obj_json.get('id'), "status": obj_json.get('text'), "created_at": obj_json.get('created_at')})
  return tweets

