#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy as tw

consumer_key= 'R84A3vsG8fMMAO4btiEehPWQD'
consumer_secret= 'ihfi2Axa00tLB7S7mrZ3DBKWg3XwP6me5kBHU4WO2hLgJHnM42'
access_token= '1309472982234849280-IAjX1txVzaNEq5mdXXPrYmg7gxAszm'
access_token_secret= 'DMoAX5ou8eOhKyjSpeaMrAvxIbJvBGz1jYJvxx4631LBx'

# get twitter auth
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth = tw.AppAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    def get_api():
    api = tw.API(auth)
    today = datetime.now().date()
    return api

