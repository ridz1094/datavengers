"""
Twitter interface controller between the Flask app and the Twitter APIs.
"""
from app import tweet_auth 
import logging
#Checking deployment
# auth = tw.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
# auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_TOKEN_SECRET'))
# api = tw.API(auth)


def post_tweets(tweet):
    logging.info("Post message on Twitter")
    return tweet_auth.get_api().update_status(tweet)._json


def delete_tweet(id):
    logging.info("Delete message on Twitter")
    return tweet_auth.get_api().destroy_status(id)._json

def fetch_my_tweets():
    logging.info("Fetch tweets of user")
    return tweet_auth.get_api().user_timeline(count=100)


def search_public_tweets(keyword):
    logging.info("Search keyword on Twitter")
    return tweet_auth.get_api().user_timeline(keyword)
