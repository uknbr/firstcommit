#!/usr/bin/env python
import platform
import os
import random
from datetime import datetime
from flask import Flask

app = Flask(__name__)

# Get OS vars
def get_var(name):
	try:
		var = os.environ[name]
	except:
		var = ""
	return var

# Config file
def get_config(param):
	try:
	    from configparser import ConfigParser
	except ImportError:
	    from ConfigParser import ConfigParser  # ver. < 3.0

	config = ConfigParser()
	config.read('config.ini')
	return config.get('app', param)

@app.route('/')
def index():
	env_who = get_var("APP_WHO")
	if not env_who:
		env_who = "Visitor"

	env_color = get_var("APP_COLOR")
	if not env_color:
		env_color = "black"

	index = "<h2>First Commit!</h2>"
	index += "<font color=\"{}\">Hello, {}.</font>".format(env_color, env_who)
	return index

@app.route('/info')
def info():
	start_date = get_config("date")
	date_begin = datetime.strptime(start_date, '%d/%m/%y')
	date_end = datetime.today()
	date_delta = date_end - date_begin
	
	information = "<p>Running from <b>{}</b></p>".format(str(platform.uname()[1]))
	information += "<p>First commit was <b>{}</b> days ago</p>".format(date_delta.days)
	return information

@app.route('/message')
def message():
	file_message = get_config("file")
	if os.path.isfile(file_message):
		message = "<p>{}</p>".format((random.choice(list(open(file_message)))))
	else:
		message = "<p>This is default message.</p>"
	return message

if __name__ == '__main__':
	app.run(use_reloader=True, host='0.0.0.0', port=1234, debug=True)
