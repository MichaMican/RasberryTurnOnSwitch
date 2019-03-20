from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def write_data():
    data = request.get_json()
    analyse(data)
    return "OK", 200
<

@app.route("/")
def index():
    return "OK", 200

#Phils Stuff
def analyse(data):
    foo = 1

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)