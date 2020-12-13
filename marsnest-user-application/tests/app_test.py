import unittest
import os
import json
from app import *
from tests import *
from unittest.mock import Mock, patch


class TestApp(unittest.TestCase):
  def setUp(self):
    os.environ["CONSUMER_KEY"] = "R84A3vsG8fMMAO4btiEehPWQD"
    os.environ["CONSUMER_SECRET"] = "ihfi2Axa00tLB7S7mrZ3DBKWg3XwP6me5kBHU4WO2hLgJHnM42"
    os.environ["ACCESS_TOKEN"] = "1309472982234849280-IAjX1txVzaNEq5mdXXPrYmg7gxAszm"
    os.environ["ACCESS_TOKEN_SECRET"] = "DMoAX5ou8eOhKyjSpeaMrAvxIbJvBGz1jYJvxx4631LBx"

  def tearDown(self):
    del os.environ["CONSUMER_KEY"]
    del os.environ["CONSUMER_SECRET"]
    del os.environ["ACCESS_TOKEN"]
    del os.environ["ACCESS_TOKEN_SECRET"]

  @patch('app.main', create = True)
  def test_main(self, mock_main):
    expected_json = {
      "statusCode": 200,
      "body": "Hello From User Application APIs!",
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    self.assertDictEqual(main({}, {}), expected_json)

  @patch('app.createUserApplication', create = True)
  def test_createUserApplication(self, mock_createUserApplication):
    response = {"message": "Application Submitted Successfully"}
    expected_json = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    result = createUserApplication({"queryStringParameters": {"user_id": 1, "uin": 1234567890, "height": 160, "weight": 60, "blood_group": "B+", "about": "I am vegetarian", "diseases": "Suffering from Low BP", "qualification": "Graduate", "address_text": "SJSU", "country":"USA", "city": "San Jose", "state": "California", "pincode": 98765, "start_date": "2020-12-01", "end_date": "2021-07-01"}}, {})
    print("Returned Result")
    print(result)
    print("Expected Result")
    print(expected_json)
    self.assertDictEqual(result, expected_json)

  @patch('app.showUserApplications', create = True)
  def test_showUserApplications(self, mock_showUserApplications):
    response = {"data": [{"id": 22, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/13/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}]
    }
    expected_json = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    result = showUserApplications({"queryStringParameters": {"email": "the@the.com"}}, {})
    print("Returned Result")
    print(result)
    print("Expected Result")
    print(expected_json)
    self.assertDictEqual(result, expected_json)

  @patch('app.showAllApplications', create = True)
  def test_showAllApplications(self, mock_showAllApplications):
    response = '{"data": [{"id": 22, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/13/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}, {"id": 21, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/13/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}, {"id": 20, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/13/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}, {"id": 19, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/12/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}, {"id": 18, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/12/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}, {"id": 17, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/12/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}, {"id": 16, "user_id": 1, "uin": "1234567890", "height": 160, "weight": 60, "blood_group": "B+", "diseases": "Suffering from Low BP", "about": "I am vegetarian", "qualification": "Graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "07/01/2021", "created_at": "12/12/2020", "user_name": "the", "user_email": "the@the.com", "user_dob": "10/01/2020"}, {"id": 1, "user_id": 9, "uin": "12121231", "height": "ul", "weight": "ul", "blood_group": "", "diseases": "ul", "about": "fasfs", "qualification": "graduate", "status": "Approved", "start_date": "12/01/2020", "end_date": "03/01/2021", "created_at": "12/03/2020", "user_name": "abc3", "user_email": "abc3@gmail.com", "user_dob": "10/01/1991"}, {"id": 3, "user_id": 11, "uin": "12121231", "height": "ul", "weight": "ul", "blood_group": "b+", "diseases": "ul", "about": "dsadasdas", "qualification": "graduate", "status": "Rejected", "start_date": "12/01/2020", "end_date": "03/01/2021", "created_at": "12/03/2020", "user_name": "abc4", "user_email": "abc4@gmail.com", "user_dob": "10/01/1991"}, {"id": 2, "user_id": 11, "uin": "12121231", "height": "ul", "weight": "ul", "blood_group": "b+", "diseases": "ul", "about": "dsadasdas", "qualification": "graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "03/01/2021", "created_at": "12/03/2020", "user_name": "abc4", "user_email": "abc4@gmail.com", "user_dob": "10/01/1991"}, {"id": 5, "user_id": 12, "uin": "3243321", "height": "ul", "weight": "ul", "blood_group": "b+", "diseases": "ul", "about": "", "qualification": "graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "03/01/2021", "created_at": "12/03/2020", "user_name": "abc5", "user_email": "abc5@gmail.com", "user_dob": "10/01/1991"}, {"id": 7, "user_id": 13, "uin": "3454643", "height": "ul", "weight": "ul", "blood_group": "", "diseases": "ul", "about": "", "qualification": "graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "03/01/2021", "created_at": "12/03/2020", "user_name": "abc6", "user_email": "abc6@gmail.com", "user_dob": "10/01/1991"}, {"id": 6, "user_id": 13, "uin": "3454643", "height": "ul", "weight": "ul", "blood_group": "", "diseases": "ul", "about": "", "qualification": "graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "03/01/2021", "created_at": "12/03/2020", "user_name": "abc6", "user_email": "abc6@gmail.com", "user_dob": "10/01/1991"}, {"id": 11, "user_id": 20, "uin": "123", "height": "ul", "weight": "ul", "blood_group": "o+", "diseases": "ul", "about": "aaa", "qualification": "Astronaut", "status": "Approved", "start_date": "01/01/2020", "end_date": "01/01/2020", "created_at": "12/04/2020", "user_name": "mg", "user_email": "mg@g.com", "user_dob": "11/11/2011"}, {"id": 9, "user_id": 28, "uin": "1234", "height": "ul", "weight": "ul", "blood_group": "A+", "diseases": "ul", "about": "I am a traveler in space", "qualification": "Graduate", "status": "Pending", "start_date": "05/05/9999", "end_date": "05/05/2031", "created_at": "12/04/2020", "user_name": "abc13", "user_email": "abc13@gmail.com", "user_dob": "10/01/1991"}, {"id": 8, "user_id": 28, "uin": "12121231", "height": "ul", "weight": "ul", "blood_group": "b+", "diseases": "ul", "about": "", "qualification": "graduate", "status": "Pending", "start_date": "12/01/2020", "end_date": "03/01/2021", "created_at": "12/04/2020", "user_name": "abc13", "user_email": "abc13@gmail.com", "user_dob": "10/01/1991"}, {"id": 10, "user_id": 45, "uin": "1234", "height": "ul", "weight": "ul", "blood_group": "A+", "diseases": "ul", "about": "Life is good!", "qualification": "Graduate", "status": "Approved", "start_date": "05/05/2021", "end_date": "05/05/2031", "created_at": "12/04/2020", "user_name": "tester1", "user_email": "tester@tester.com", "user_dob": "04/22/1990"}, {"id": 12, "user_id": 46, "uin": "1234", "height": "ul", "weight": "ul", "blood_group": "A+", "diseases": "ul", "about": "I am a traveler ", "qualification": "Graduate", "status": "Approved", "start_date": "05/05/2021", "end_date": "05/05/2031", "created_at": "12/04/2020", "user_name": "tester12", "user_email": "tester1@tester.com", "user_dob": "11/22/1990"}, {"id": 13, "user_id": 47, "uin": "1234", "height": "ul", "weight": "ul", "blood_group": "A+", "diseases": "ul", "about": "dd", "qualification": "Graduate", "status": "Rejected", "start_date": "05/05/2021", "end_date": "05/05/2031", "created_at": "12/05/2020", "user_name": "tester1234", "user_email": "testing@test.com", "user_dob": "04/22/1990"}, {"id": 14, "user_id": 50, "uin": "1234", "height": "ul", "weight": "ul", "blood_group": "A+", "diseases": "ul", "about": "i m a traveler", "qualification": "Graduate", "status": "Approved", "start_date": "05/05/2021", "end_date": "05/05/2031", "created_at": "12/05/2020", "user_name": "dd12", "user_email": "dd@dd.com", "user_dob": "04/22/1990"}, {"id": 15, "user_id": 51, "uin": "1234", "height": "ul", "weight": "ul", "blood_group": "A+", "diseases": "ul", "about": "its me", "qualification": "Graduate", "status": "Approved", "start_date": "05/05/2021", "end_date": "05/05/2031", "created_at": "12/05/2020", "user_name": "demo", "user_email": "demo@demo.com", "user_dob": "04/22/1990"}]}'

    expected_json = {
      "statusCode": 200,
      "body": response,
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    result = showAllApplications({}, {})
    print("Expected Result")
    print(len(result['body']))
    print("Returned Result")
    print(len(expected_json["body"]))
    self.assertEqual(len(result['body']), len(expected_json["body"]))


  @patch('app.createUser', create = True)
  def test_createUser(self, mock_createUser):
    response = {"message": "User Created Successfully"}
    expected_json = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    result = createUser({"queryStringParameters": {"name": "dd", "email": "dd@gmail.com", "dob": "2020-10-01", "mobile": 999999999, "token": "gyguihoijilj"}}, {})
    print("Returned Result")
    print(result)
    print("Expected Result")
    print(expected_json)
    self.assertDictEqual(result, expected_json)

  @patch('app.getUserByEmail', create = True)
  def test_getUserByEmail(self, mock_getUserByEmail):
    response = {"data": {"id": 52, "name": "xyz", "email": "xyz@gmail.com", "dob": "10/01/2020", "mobile": "999999999", "token": "null", "role": "visitor", "created_at": "12/13/2020"}}
    expected_json = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
      },
      "isBase64Encoded": False
    }
    result = getUserByEmail({"queryStringParameters": {"email": "xyz@gmail.com"}}, {})
    print("Returned Result")
    print(result['body'])
    print("Expected Result")
    print(expected_json["body"])
    self.assertEqual(result['body'], expected_json["body"])