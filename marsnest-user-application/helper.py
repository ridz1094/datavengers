from flask import request

def extract_user_application_object(request, user_id):
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
  return user_application

def format_response(response):
  results = []
  for row in response:
    t = {'id': row[0], 'user_id': row[1], 'uin': row[2], 'height': row[3], 'weight': row[4], 'blood_group': row[5], 'diseases': row[6], 'about': row[7], 'qualification': row[8], 'status': row[9], 'start_date': row[10].strftime("%m/%d/%Y"), 'end_date': row[11].strftime("%m/%d/%Y"), 'created_at': row[12].strftime("%m/%d/%Y")}
    results.append(t)
  return results