#!/usr/bin/env python
import platform
import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = "<h2>Hello, Infra. {0}</h2>".format(os.environ['CUSTOM_MESSAGE'])
    return message

@app.route('/info')
def info():

	with open('date.conf') as f:
		start_date = f.readline()

	date_begin = datetime.strptime(start_date, '%d/%m/%y')
	date_end = datetime.today()
	date_delta = date_end - date_begin
	
	information = "<p>Running from <b>{}</b></p><p>First commit was <b>{}</b> days ago</p>".format(str(platform.uname()[1]), date_delta.days)
	return information

if __name__ == '__main__':
	app.run(use_reloader=True, host='0.0.0.0', port=1234, debug=True)