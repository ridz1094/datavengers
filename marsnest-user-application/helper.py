from flask import request

def extract_user_application_object(request, user_id):
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

  return user_application
