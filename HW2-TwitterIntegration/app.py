from flask import Flask, request, jsonify
import tweepy as tw

from twitter import *

app = Flask(__name__)

@app.route("/") 
def home():
  return "Hello! this is Twitter API Integration!" 

@app.route('/tweet', methods=["POST"])
def create():
  tweet_msg = request.json.get("message")
  post_tweet(tweet_msg)
  message = "Posted tweet on twitter."
  return jsonify({"message": message})

@app.route('/tweet/<id>', methods=["DELETE"])
def delete(id):
  delete_tweet(id)
  return jsonify({"message": "Deleted tweet on twitter."})

@app.route('/my_tweets', methods=["GET"])
def show():
  result = display_tweets()
  return jsonify({"data": result})

@app.route('/tweets', methods=["GET"])
def search():
  search_string = request.args.get('query')
  result = search_tweet(search_string)
  return jsonify({"data": result})

