import unittest
import os
import json
from handler import *
from tests import *
from unittest.mock import Mock, patch


class TestHandler(unittest.TestCase):

  def setUp(self):
    os.environ["CONSUMER_KEY"] = "R84A3vsG8fMMAO4btiEehPWQD"
    os.environ["CONSUMER_SECRET"] = "ihfi2Axa00tLB7S7mrZ3DBKWg3XwP6me5kBHU4WO2hLgJHnM42"
    os.environ["ACCESS_TOKEN"] = "1309472982234849280-IAjX1txVzaNEq5mdXXPrYmg7gxAszm"
    os.environ["ACCESS_TOKEN_SECRET"] = "DMoAX5ou8eOhKyjSpeaMrAvxIbJvBGz1jYJvxx4631LBx"

  def tearDown(self):
    del os.environ["CONSUMER_KEY"]
    del os.environ["CONSUMER_SECRET"]
    del os.environ["ACCESS_TOKEN"]
    del os.environ["ACCESS_TOKEN_SECRET"]

  @patch('handler.postTweet', create = True)
  def test_postTweet(self, mock_postTweet):
    response = {'created_at': 'Sun Oct 04 17:51:57 +0000 2020', 'id': 1312812716420079617, 'id_str': '1312812716420079617', 'text': 'New Text Messagee for test4!!', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 1310855986823847937, 'id_str': '1310855986823847937', 'name': 'princy', 'screen_name': 'princy40269170', 'location': '', 'description': '', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 0, 'friends_count': 0, 'listed_count': 0, 'created_at': 'Tue Sep 29 08:16:44 +0000 2020', 'favourites_count': 0, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 20, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': True, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'fr'}

    mock_postTweet.return_value = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
          'Access-Control-Allow-Headers': 'Content-Type',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    expected_json = {
      "statusCode": 400,
      "body": dict(response),
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    result = postTweet({"queryStringParameters": { "message": "New Text Messagee for test4!!"}}, {})
    print("Returned Result")
    print(result['body'])
    print("Expected Result")
    print(expected_json['body'])
    self.assertDictEqual(result['body'], expected_json['body'])

  @patch('handler.deleteTweet', create = True)
  def test_deleteTweet(self, mock_deleteTweet):
    response = {'created_at': 'Sun Oct 04 15:55:32 +0000 2020', 'id': 1312783422826274816, 'id_str': '1312783422826274816', 'text': 'ABC', 'truncated': False}

    mock_deleteTweet.return_value = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
          'Access-Control-Allow-Headers': 'Content-Type',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }

    expected_json = {
      "statusCode": 400,
      "body": '',
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    self.assertDictEqual(deleteTweet({"queryStringParameters": {"id": 1312783422826274816}}, {})['body'], expected_json['body'])

  @patch('handler.displayTweet', create = True)
  def test_displayTweet(self, mock_displayTweet):
    response = [{'created_at': 'Thu Oct 01 07:26:18 +0000 2020', 'id': 1311568104774750208, 'id_str': '1311568104774750208', 'text': 'Science Keyword included!', 'truncated': False}]

    mock_displayTweet.return_value = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
          'Access-Control-Allow-Headers': 'Content-Type',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }

    expected_json = {
      "statusCode": 400,
      "body": '',
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    self.assertDictEqual(displayTweet({}, {}), expected_json)

  @patch('handler.searchTweet', create = True)
  def test_searchTweet(self, mock_searchTweet):
    response = [{'created_at': 'Thu Oct 01 07:26:18 +0000 2020', 'id': '1311568104774750208', 'id_str': '1311568104774750208', 'text': 'Science Keyword included!', 'truncated': False}]

    mock_searchTweet.return_value = {
      "statusCode": 200,
      "body": response,
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }

    expected_json = {
      "statusCode": 400,
      "body": '',
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    self.assertDictEqual(searchTweet({"queryStringParameters": { "keyword": "Science Keyword included!"}}, {}), expected_json)


if __name__ == '__main__':
  unittest.main()