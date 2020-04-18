from flask import Flask, request
import json
from create_db import *

app = Flask(__name__)

@app.route('/')
def index():
	return """<html>
	<head><title>Flask Store API | By SpeedX</title></head>
	<style>
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
            width: 100%;
        }
        body {
            display: table;
        }
        .centered-text {
            text-align: center;
            display: table-cell;
            vertical-align: middle;
        }
        </style>
	<body style="background:#000000">
  <div class="centered-text"><h1><font color="#00ff00">
  <u>This is A Simple Flask API To Store User Data By SpeedX </u>
  </font></h1><br><br>
  <font color="#00ffff">
  <h3>
  NOTE: This is totally insecure and just a example
  </h3>
  </font><br><br><br>
  <h4><font color="#ff0000">
Made With ❤ By   <a href="https://github.com/TheSpeedX">SpeedX</a>
  </font></h4>
  </div></body></html>"""

@app.route('/api/create',methods=['POST'])
def make_user():
	data=request.get_json()
	try:
		email=data['email']
		phone=data['phone']
		username=data['username']
		response=create_user(email,phone,username)
	except:
		response={"success": False}
	return json.dumps(response)

@app.route('/api/fetch',methods=['POST'])
def fetch_user():
	data=request.get_json()
	try:
		email=data.get('email',None)
		phone=data.get('phone',None)
		response=fetch_data(email,phone)
	except:
		response={"email":"", "phone": "", "username": ""}
	return json.dumps(response)

app.run(debug=True)