# username - postgres
# password - xQw82gWFmCL9SfkDmdqy

from datetime import date
import sys
import logging
import psycopg2
import json

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
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

# def drop_table():
#   with connection.cursor() as cur:
#     cur.execute("""drop table user_applications""")
#   connection.commit()
#   return True

# def create_user_table():
#   with connection.cursor() as cur:
#     cur.execute("""create table if not exists users (id SERIAL PRIMARY KEY not null, name varchar(50), email varchar(50) not null UNIQUE, mobile integer, password varchar(50), role varchar(50), token varchar(255), dob date, created_at timestamp not null)""")
#   connection.commit()
#   return True

# def create_table():
#   with connection.cursor() as cur:
    # cur.execute("""create table if not exists user_applications (id SERIAL PRIMARY KEY not null, user_id int, uin varchar(10) not null, height int, weight int, blood_group varchar(5), diseases varchar(255), about varchar(255), qualification varchar(255), status varchar(255) not null, start_date date not null, end_date date not null, address_text varchar(255), country varchar(255), city varchar(255), state varchar(255), pincode varchar(255), created_at timestamp not null,CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id))""")
#   connection.commit()
#   return True


def update_user_applications(user_obj):
    response = "Null"
    with connection.cursor() as cur:
        print("Execute Query")
        query = "UPDATE user_applications SET status = %s WHERE id = %s"
        print("---------")
        print(query)
        cur.execute(query, (user_obj.get('status'), user_obj.get('id')))
        response = "User application status updated Successfully"
    connection.commit()
    return response