#!/usr/bin/python

from flask import Flask, request
import os, json

app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT"))

@app.route('/')
def home():
	port = os.getenv("VCAP_APP_PORT")
	apps = json.loads(os.getenv("VCAP_APPLICATION"))
	serv = os.getenv("VCAP_SERVICES")
	return json.dumps({'VCAP_APP_PORT': port, 
		'VCAP_APPLICATION':apps, 'VCAP_SERVICES':serv })

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=port)


