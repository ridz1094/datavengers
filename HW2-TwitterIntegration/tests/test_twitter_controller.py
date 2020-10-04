import unittest
from unittest.mock import Mock, patch
from app import twitter_controller as tc

class TestTwitterController(unittest.TestCase):
  
  @patch('app.twitter_controller.post_tweet', create = True)
  def test_post_tweet(self, mock_post_tweet):
    mock_post_tweet.return_value = {'created_at': 'Sun Oct 04 17:51:57 +0000 2020', 'id': 1312812716420079617, 'id_str': '1312812716420079617', 'text': 'New Text Messagee!!', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 1310855986823847937, 'id_str': '1310855986823847937', 'name': 'princy', 'screen_name': 'princy40269170', 'location': '', 'description': '', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 0, 'friends_count': 0, 'listed_count': 0, 'created_at': 'Tue Sep 29 08:16:44 +0000 2020', 'favourites_count': 0, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 20, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': True, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'fr'}

    response = tc.post_tweet("New Text Messagee!!")

    self.assertEqual(response['text'], "New Text Messagee!!")

  @patch('app.twitter_controller.delete_tweet', create = True)
  def test_delete_tweet(self, mock_delete_tweet):
    mock_delete_tweet.return_value = {'created_at': 'Sun Oct 04 15:55:32 +0000 2020', 'id': 1312783422826274816, 'id_str': '1312783422826274816', 'text': 'ABC', 'truncated': False}
    response = tc.delete_tweet(1312783422826274816)

    self.assertEqual(response['id'], 1312783422826274816)

  @patch('app.twitter_controller.search_public_tweets', create = True)
  def test_search_public_tweets(self, mock_search_public_tweets):
    mock_search_public_tweets.return_value = [{'created_at': 'Thu Oct 01 07:26:18 +0000 2020', 'id': 1311568104774750208, 'id_str': '1311568104774750208', 'text': 'Science Keyword included!', 'truncated': False}]
    response = tc.search_public_tweets("Science Keyword included!")
    self.assertEqual(len(response), 1)

  @patch('app.twitter_controller.fetch_my_tweets', create = True)
  def test_fetch_my_tweets(self, mock_fetch_my_tweets):
    mock_fetch_my_tweets.return_value = [{'created_at': 'Thu Oct 01 07:26:18 +0000 2020', 'id': 1311568104774750208, 'id_str': '1311568104774750208', 'text': 'Science Keyword included!', 'truncated': False}]
    response = tc.search_public_tweets("Science Keyword included!")
    response = tc.fetch_my_tweets()
    self.assertEqual(len(response), 1)
  
if __name__ == '__main__':
    unittest.main()
