import os
import postgres as pg
from datetime import date
import status
import json

from flask import Flask, request
app = Flask(__name__)

USERS_APPLICATION_TABLE = os.environ['USERS_APPLICATION_TABLE']

# @app.route("/")
def hello(event, context):
  return {
    "statusCode": 200,
    "body": "Hello World!",
    "headers": {},
    "isBase64Encoded": False
  }

# @app.route("/user_application", methods=["POST"])
def createUserApplication(event, context):
  statusCode = 200
  result = {}
  try:
    user_id = event["user_id"]
    uin = event["uin"]
    start_date = event["start_date"]
    end_date = event["end_date"]
    height = event["height"] or "NULL"
    weight = event["weight"] or "NULL"
    blood_group = event["blood_group"] or "NULL"
    about = event["about"] or "NULL"
    diseases = event["diseases"] or "NULL"
    qualification = event["qualification"] or "NULL"

    user_application = {"userId": user_id, "uin": uin, "status": Status.Pending.name, "start_date": start_date, "end_date": end_date, "created_at": date.today(), "height": height, "weight": weight, "qualification": qualification, "about": about, "diseases": diseases, "blood_group": blood_group, "created_at": date.today()}

    # user_application = extract_user_application_object(request, user_id)
    pg.create_user_applicaitons(user_application)
    result = "Application Submitted Successfully"
  except e:
    statusCode = 400
    result = json.dumps(handle_exception(e))

  return {
    "statusCode": statusCode,
    "body": "Application Submitted Successfully",
    "headers": {},
    "isBase64Encoded": False
  }

# @app.route("/user/user_applications")
def showUserApplications(event, context):
  statusCode = 200
  result = {}
  try:
    result = pg.show_user_applications(event["user_id"])
  except:
    statusCode = 400
    result = {"error": "Error while fetching values from Db"}
  
  return {
    "statusCode": statusCode,
    "body": json.dumps(result),
    "headers": {},
    "isBase64Encoded": False
  }

@app.route("/user_applications")
def showAllApplications(event, context):
  statusCode = 200
  result = {}
  try:
    result = pg.show_all_applications()
  except:
    statusCode = 400
    result = {"error": "Error while getting value from Db"}
  
  return {
    "statusCode": statusCode,
    "body": json.dumps(result),
    "headers": {},
    "isBase64Encoded": False
  }

def handle_exception(e):
    return e.response.text
