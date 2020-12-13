import os
import postgres as pg
from datetime import date
import status
import json
import logging
import helper
import status
import role
from urllib import parse

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

# @app.route("/user_applications", methods=["POST"])
def createUserApplication(event, context):
  statusCode = 200
  result = {}
  try:
    user_id = event["queryStringParameters"]["user_id"] if 'user_id' in event["queryStringParameters"] else None
    uin = event["queryStringParameters"]["uin"] if 'uin' in event["queryStringParameters"] else None
    start_date = event["queryStringParameters"]["start_date"] if 'start_date' in event["queryStringParameters"] else None
    end_date = event["queryStringParameters"]["end_date"] if 'end_date' in event["queryStringParameters"] else None
    height = event["queryStringParameters"]["height"] if 'height' in event["queryStringParameters"] else None
    weight = event["queryStringParameters"]["weight"] if 'weight' in event["queryStringParameters"] else None
    blood_group = event["queryStringParameters"]["blood_group"] if 'blood_group' in event["queryStringParameters"] else None
    about = event["queryStringParameters"]["about"] if 'about' in event["queryStringParameters"] else None
    diseases = event["queryStringParameters"]["diseases"] if 'diseases' in event["queryStringParameters"] else None
    qualification = event["queryStringParameters"]["qualification"] if 'qualification' in event["queryStringParameters"] else None
    address = event["queryStringParameters"]["address"] if 'address' in event["queryStringParameters"] else None
    country = event["queryStringParameters"]["country"] if 'country' in event["queryStringParameters"] else None
    city = event["queryStringParameters"]["city"] if 'city' in event["queryStringParameters"] else None
    state = event["queryStringParameters"]["state"] if 'state' in event["queryStringParameters"] else None
    pincode = event["queryStringParameters"]["pincode"] if 'pincode' in event["queryStringParameters"] else None
    
    user_application = {"user_id": user_id, "uin": uin, "status": status.Status.Pending.name, "start_date": start_date, "end_date": end_date, "created_at": date.today(), "height": height, "weight": weight, "qualification": qualification, "about": about, "diseases": diseases, "blood_group": blood_group, "address_text": address, "country": country, "city": city, "state": state, "pincode": pincode}
    
    pg.create_user_applicaitons(user_application)
    result = {"message": "Application Submitted Successfully"}
  except:
    statusCode = 400
    result = {"error": "Error while registring for user application"}

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

# @app.route("/user/user_applications")
def showUserApplications(event, context):
  statusCode = 200
  result = {}
  try:
    email = parse.unquote(event["queryStringParameters"]["email"]) if 'email' in event["queryStringParameters"] else None
    result = {"data": pg.show_user_applications(email)}
  except:
    statusCode = 400
    result = {"error": "Error while fetching records of user application"}
  
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

# @app.route("/user_applications")
def showAllApplications(event, context):
  statusCode = 200
  result = {}
  try:
    result = {"data": pg.show_all_applications()}
  except:
    statusCode = 400
    result = {"error": "Error while fetching records"}
  
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


# @app.route("/user_application")
def getUserApplication(event, context):
  statusCode = 200
  result = {}
  try:
    result = {"data": pg.get_user_application(event["queryStringParameters"]["user_application_id"])}
  except:
    statusCode = 400
    result = {"error": "Error while fetching records"}
  
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

# @app.route("/users", methods=["GET"])
def createUser(event, context):
  statusCode = 200
  result = {}
  try:
    name = event["queryStringParameters"]["name"] if 'name' in event["queryStringParameters"] else None
    email = parse.unquote(event["queryStringParameters"]["email"]) if 'email' in event["queryStringParameters"] else None
    mobile = event["queryStringParameters"]["mobile"] if 'mobile' in event["queryStringParameters"] else None
    password = event["queryStringParameters"]["password"] if 'password' in event["queryStringParameters"] else None
    token = event["queryStringParameters"]["token"] if 'token' in event["queryStringParameters"] else None
    dob = event["queryStringParameters"]["dob"] if 'dob' in event["queryStringParameters"] else None
    user_role = role.Role.visitor.name
    user = {"name": name, "email": email, "mobile": mobile, "password": password, "role": user_role, "token": token, "created_at": date.today(), "dob": dob}
    print(user)
    pg.create_user(user)
    result = {"message": "User Created Successfully"}
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

# @app.route("/users/id")
def getUserById(event, context):
  statusCode = 200
  result = {}
  try:
    result = {"data": pg.get_user_by_id(event["queryStringParameters"]["id"])}
  except:
    statusCode = 400
    result = {"error": "Error while fetching records"}
  
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

# @app.route("/users/email")
def getUserByEmail(event, context):
  statusCode = 200
  result = {}
  try:
    email = parse.unquote(event["queryStringParameters"]["email"])
    print(email)
    result = {"data": pg.get_user_by_email(email)}
  except:
    statusCode = 400
    result = {"error": "Error while fetching records"}
  
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

# @app.route("/users")
def updateUser(event, context):
  statusCode = 201
  result = {}
  try:
    email = parse.unquote(event["queryStringParameters"]["email"]) if 'email' in event["queryStringParameters"] else None
    mobile = event["queryStringParameters"]["mobile"] if 'mobile' in event["queryStringParameters"] else None
    password = event["queryStringParameters"]["password"] if 'password' in event["queryStringParameters"] else None
    token = event["queryStringParameters"]["token"] if 'token' in event["queryStringParameters"] else None
    dob = event["queryStringParameters"]["dob"] if 'dob' in event["queryStringParameters"] else None

    user = {"token": token, "email": email, "dob": dob, "mobile": mobile}
    print(user)
    pg.update_user(user)
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