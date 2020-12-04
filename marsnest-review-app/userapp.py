import os
#import postgres as pg
from datetime import date
#import status
import json
import logging
#import helper
#import status
#import role
from urllib import parse
import reviewapp as ra 
from flask import Flask, request
app = Flask(__name__)
USERS_APPLICATION_TABLE = "user_applications"

# @app.route("/")
def main(event, context):
  return {
    "statusCode": 200,
    "body": "Hello From User Application APIs!",
    "headers": {
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
    },
    "isBase64Encoded": False
  }

  # @app.route("/")
def updateUserApplications(event, context):
  statusCode = 201
  result = {}
  try:
    status = event["queryStringParameters"]["status"] if 'status' in event["queryStringParameters"] else None
    id = event["queryStringParameters"]["id"] if 'id' in event["queryStringParameters"] else None
    print(status)
    print(id)
    user = {"status": status, "id": id}
    print(user)
    ra.update_user_applications(user)
    result = {"message": "User Updated Successfully"}
  except:
    statusCode = 400
    result = {"error": "Error while creating user"}

  return {
    "statusCode": statusCode,
    "body": json.dumps(result),
    "headers": {
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
    },
    "isBase64Encoded": False
  }