#!/usr/bin/python

from flask import Flask, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__,static_url_path='')
port = int(os.getenv("VCAP_APP_PORT"))

@app.route('/')
	return port

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=port)


