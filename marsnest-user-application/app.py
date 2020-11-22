import os
import postgres as pg
from datetime import date
import status

from flask import Flask, request
app = Flask(__name__)

USERS_APPLICATION_TABLE = os.environ['USERS_APPLICATION_TABLE']

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/users/<string:user_id>/user_application", methods=["POST"])
def createUserApplication(user_id):
  statusCode = 200
  result = {}
  try:
    uin = request.json.get('uin') 
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    height = request.json.get('height') or "NULL"
    weight = request.json.get('weight') or "NULL"
    blood_group = request.json.get('blood_group') or "NULL"
    about = request.json.get('about') or "NULL"
    diseases = request.json.get('diseases') or "NULL"
    qualification = request.json.get('qualification') or "NULL"

    user_application = {"userId": user_id, "uin": uin, "status": Status.Pending.name, "start_date": start_date, "end_date": end_date, "created_at": date.today(), 'height': height, 'weight': weight, 'qualification': qualification, 'about': about, 'diseases': diseases, 'blood_group': blood_group, 'created_at': date.today()}

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

@app.route("/users/<string:user_id>/user_application")
def showUserApplications(user_id):
  statusCode = 200
  result = {}
  try:
    result = pg.show_user_applications(user_id)
  except e:
    statusCode = 400
    result = handle_exception(e)
  
  return {
    "statusCode": statusCode,
    "body": json.dumps(result),
    "headers": {},
    "isBase64Encoded": False
  }

@app.route("/user_applications")
def showAllApplications():
  statusCode = 200
  result = {}
  try:
    result = pg.show_all_applications()
  except e:
    statusCode = 400
    result = handle_exception(e)
  
  return {
    "statusCode": statusCode,
    "body": json.dumps(result),
    "headers": {},
    "isBase64Encoded": False
  }

def handle_exception(e):
    return e.response.text
