import os
import tweepy as tw

consumer_key= 'R84A3vsG8fMMAO4btiEehPWQD'
consumer_secret= 'ihfi2Axa00tLB7S7mrZ3DBKWg3XwP6me5kBHU4WO2hLgJHnM42'
access_token= '1309472982234849280-IAjX1txVzaNEq5mdXXPrYmg7gxAszm'
access_token_secret= 'DMoAX5ou8eOhKyjSpeaMrAvxIbJvBGz1jYJvxx4631LBx'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def post_tweet(api):
  print("Posting tweet on twitter")
  api.update_status("Hello, I am posting my first tweet from Python code! #firstpost")

def main():
  api = tw.API(auth, wait_on_rate_limit=True)
  post_tweet(api)

main()