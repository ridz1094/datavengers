# import json
# from flask import render_template
# import unittest
# from unittest.mock import Mock, patch
# # from app import twitter_controller as tc


# def test_home(app, client):
#     res = client.get('/')
#     assert res.status_code == 200
#     expected = render_template(
#         "home.html",
#         active_tab='home')
#     assert expected == json.loads(res.get_data(as_text=True))