# -*- coding: utf-8 -*-
import tweepy as tw
import os

# Set variable on local terminal or add it in environment variables
# export CONSUMER_KEY=R84A3vsG8fMMAO4btiEehPWQD
# export CONSUMER_SECRET=ihfi2Axa00tLB7S7mrZ3DBKWg3XwP6me5kBHU4WO2hLgJHnM42
# export ACCESS_TOKEN=1309472982234849280-IAjX1txVzaNEq5mdXXPrYmg7gxAszm
# export ACCESS_TOKEN_SECRET=DMoAX5ou8eOhKyjSpeaMrAvxIbJvBGz1jYJvxx4631LBx

auth = tw.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_TOKEN_SECRET'))

def get_api():
  api = tw.API(auth, wait_on_rate_limit=True)
  return api
