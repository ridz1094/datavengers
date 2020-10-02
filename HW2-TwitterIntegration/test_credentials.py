#!/usr/bin/env python
import os
import tweepy as tw

# Authenticate to Twitter
auth = tw.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_TOKEN_SECRET'))
api = tw.API(auth)

try:
    api.verify_credentials()
    print("Authentication is OK")
except:
    print("We have encountered an error during authentication")

