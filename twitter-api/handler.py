import json
import tweepy
import tweet_auth

# from flask import Flask, request
# app = Flask(__name__)

# @app.route("/tweet/post", methods=["POST"])
def postTweet(event, context):
  statusCode = 200
  result = {}
  try:
    result = tweet_auth.get_api().update_status(event["queryStringParameters"]["message"])
  except tweepy.TweepError as e:
    print(e)
    statusCode = 400
    result = ''

  response = {
    "statusCode": statusCode,
    "body": json.dumps(result),
    "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
    },
    "isBase64Encoded": False
  }
  return response


def displayTweet(event, context):
  statusCode = 200
  result = {}
  try:
    result = tweet_auth.get_api().user_timeline(count=100)
  except tweepy.TweepError as e:
    statusCode = 400
    result = handle_exception(e)
  response = {
    "statusCode": statusCode,
    "body": json.dumps(result),
    "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
    },
    "isBase64Encoded": False
  }
  return response


def deleteTweet(event, context):
    statusCode = 200
    result = {}
    try:
        result = tweet_auth.get_api().destroy_status(event["queryStringParameters"]["id"])
    except tweepy.TweepError as e:
        statusCode = 400
        result = handle_exception(e)
    response = {
      "statusCode": statusCode,
      "body": json.dumps(result),
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    return response


def searchTweet(event, context):
    statusCode = 200
    result = {}
    try:
        result = tweet_auth.get_api().user_timeline(event["queryStringParameters"]["keyword"])
    except tweepy.TweepError as e:
        statusCode = 400
        result = handle_exception(e)
    response = {
      "statusCode": statusCode,
      "body": json.dumps(result),
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    return response

def handle_exception(e):
    return e.response
