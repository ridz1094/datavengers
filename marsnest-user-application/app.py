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
    user_application_params = json.loads(event["body"])
    # user_application_params = request.json
    user_id = user_application_params.get("user_id")
    uin = user_application_params.get("uin")
    start_date = user_application_params.get("start_date")
    end_date = user_application_params.get("end_date")
    height = user_application_params.get("height")
    weight = user_application_params.get("weight")
    blood_group = user_application_params.get("blood_group")
    about = user_application_params.get("about")
    diseases = user_application_params.get("diseases")
    qualification = user_application_params.get("qualification")
    address_text = user_application_params.get("address_text")
    country = user_application_params.get("country")
    city = user_application_params.get("city")
    state = user_application_params.get("state")
    pincode = user_application_params.get("pincode")
    
    user_application = {"user_id": user_id, "uin": uin, "status": status.Status.Pending.name, "start_date": start_date, "end_date": end_date, "created_at": date.today(), "height": height, "weight": weight, "qualification": qualification, "about": about, "diseases": diseases, "blood_group": blood_group, "address_text": address_text, "country": country, "city": city, "state": state, "pincode": pincode}
    
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
    result = {"data": pg.show_user_applications(event["queryStringParameters"]["user_id"])}
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

# @app.route("/users", methods=["POST"])
def createUser(event, context):
  statusCode = 200
  result = {}
  try:
    breakpoint()
    user_params = json.loads(event["body"])
    # user_params = request.json
    name = user_params.get("name")
    email = user_params.get("email")
    mobile = user_params.get("mobile")
    password = user_params.get("password")
    user_role = role.Role.visitor.name
    token = user_params.get("token")
    dob = user_params.get("dob")

    user = {"name": name, "email": email, "mobile": mobile, "password": password, "role": user_role, "token": token, "created_at": date.today()}
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
    user_params = json.loads(event["body"])
    # user_params = request.json
    token = user_params.get("token")
    email = user_params.get("email")

    user = {"token": token, "email": email}
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