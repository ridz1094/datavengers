# username - postgres
# password - xQw82gWFmCL9SfkDmdqy

from datetime import date
import sys
import logging
import psycopg2
import helper

#rds settings
rds_host  = 'marsnest.cqjxjq7sdnq5.us-east-1.rds.amazonaws.com'
name = 'postgres'
password = 'xQw82gWFmCL9SfkDmdqy'
db_name = 'marsnest'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
  connection = psycopg2.connect(host = rds_host, port = 5432, user = name, password = password)
  cursor=connection.cursor()
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

# def drop_table():
#   with connection.cursor() as cur:
#     cur.execute("""drop table user_applications""")
#   connection.commit()
#   return True

# def create_user_table():
#   with connection.cursor() as cur:
#     cur.execute("""create table if not exists users (id SERIAL PRIMARY KEY not null, name varchar(50), email varchar(50) not null UNIQUE, mobile integer, password varchar(50), role varchar(50), token varchar(255), created_at timestamp not null)""")
#   connection.commit()
#   return True

# def create_table():
#   with connection.cursor() as cur:
#     cur.execute("""create table if not exists user_applications (id SERIAL PRIMARY KEY not null, user_id int, uin varchar(10) not null, height int, weight int, blood_group varchar(5), diseases varchar(255), about varchar(255), qualication varchar(255), status varchar(255) not null, start_date date not null, end_date date not null, created_at timestamp not null,
#     CONSTRAINT fk_user
#       FOREIGN KEY(user_id) 
# 	      REFERENCES users(id))""")
#   connection.commit()
#   return True

def create_user_applicaitons(user_application):
  response = "Null"
  with connection.cursor() as cur:
    print("Execute Query")
    query = f"INSERT INTO user_applications (user_id, uin, height, weight, blood_group, diseases, about, qualication, status, start_date, end_date, created_at) VALUES ( {user_application['userId']}, {user_application['uin']}, {user_application['height']}, {user_application['weight']}, {user_application['blood_group']}, {user_application['diseases']}, {user_application['about']}, {user_application['qualification']}, '{user_application['status']}', '{user_application['start_date']}','{user_application['end_date']}','{user_application['created_at']}')"
    print(query)
    response = cur.execute(query)
  connection.commit()
  return response

def show_user_applications(user_id):
  response = "Null"
  results = []
  with connection.cursor() as cur:
    print("Select Query")
    query = f"SELECT id, user_id, uin, height, weight, blood_group, diseases, about, qualication, status, start_date, end_date, created_at FROM user_applications WHERE user_id = {user_id}"
    cur.execute(query)
    response = cur.fetchall()
    results = helper.format_response(response)
  connection.commit()
  return results

def show_all_applications():
  response = "Null"
  results = []
  with connection.cursor() as cur:
    print("Select Query")
    query = f"SELECT id, user_id, uin, height, weight, blood_group, diseases, about, qualication, status, start_date, end_date, created_at FROM user_applications"
    cur.execute(query)
    response = cur.fetchall()
    results = helper.format_response(response)
  connection.commit()
  return results


