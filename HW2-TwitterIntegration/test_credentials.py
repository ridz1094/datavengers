#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy as tw

# Authenticate to Twitter
auth = twy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

try:
    api.verify_credentials()
    print("Authentication is OK")
except:
    print("We have encountered an error during authentication")

