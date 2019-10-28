#!/usr/bin/env python
import platform
import os
import redis
from flask import Flask

app = Flask(__name__)

redis_db = redis.StrictRedis(host="cache", port=6379, db=0)

@app.route('/')
def index():
    message = "<h2>Hello, Infra. {0}</h2>".format(os.environ['CUSTOM_MESSAGE'])
    return message

@app.route('/version')
def version():
    message = "<h3>First Commit: {0}</h3>".format(os.environ['APP_VERSION'])
    return message

@app.route('/infra')
def infra():
	redis_db.incr('hits')

	information = "<h1>Infra, please check!</h1><p>Running from <b>{}</b></p><p>Access number <b>{}</b></p>".format(str(platform.uname()[1]), redis_db.get('hits').decode("utf-8"))
	return information

if __name__ == '__main__':
	app.run(use_reloader=True, host='0.0.0.0', port=1234, debug=True)