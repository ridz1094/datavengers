#helper.py
from datetime import date
import json

def extract_user_application_object(user_application_params):
  user_application_params = json.loads(user_application_params)
  user_id = user_application_params["user_id"]
  uin = user_application_params["uin"]
  start_date = user_application_params["start_date"]
  end_date = user_application_params["end_date"]
  height = user_application_params["height"] or "NULL"
  weight = user_application_params["weight"] or "NULL"
  blood_group = user_application_params["blood_group"] or "NULL"
  about = user_application_params["about"] or "NULL"
  diseases = user_application_params["diseases"] or "NULL"
  qualification = user_application_params["qualification"] or "NULL"

  user_application = {"user_id": user_id, "uin": uin, "status": Status.Pending.name, "start_date": start_date, "end_date": end_date, "created_at": date.today(), "height": height, "weight": weight, "qualification": qualification, "about": about, "diseases": diseases, "blood_group": blood_group}
  return user_application

def format_response(response):
  results = []
  for row in response:
    t = {'id': row[0], 'user_id': row[1], 'uin': row[2], 'height': row[3], 'weight': row[4], 'blood_group': row[5], 'diseases': row[6], 'about': row[7], 'qualification': row[8], 'status': row[9], 'start_date': row[10].strftime("%m/%d/%Y"), 'end_date': row[11].strftime("%m/%d/%Y"), 'created_at': row[12].strftime("%m/%d/%Y"), 'user_name': row[13], 'user_email': row[14], 'user_dob': row[15].strftime("%m/%d/%Y")}
    results.append(t)
  return results

def format_user_response(response):
  result = ''
  for row in response:
    t = {'id': row[0], 'name': row[1], 'email': row[2], 'dob': row[3].strftime("%m/%d/%Y"), 'mobile': row[4], 'token': row[5], 'role': row[6], 'created_at': row[7].strftime("%m/%d/%Y")}
    result = t
  return result