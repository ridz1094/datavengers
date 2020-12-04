import tweepy as tw
import os

auth = tw.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_TOKEN_SECRET'))

def get_api():
  api = tw.API(auth, wait_on_rate_limit=True, parser=tw.parsers.JSONParser())
  return api
