from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
#import RPi.GPIO as GPIO

app = Flask(__name__)
CORS(app)

@app.route("/write", methods=['POST'])
def write_data():
    data = request.get_json()
    with open(statusJSONFile, 'w') as f:
        f.write(json.dumps(data))
    analyse(data)
    return "OK"

@app.route("/notAus", methods=['POST'])
def notAus():
    foo = data
    

@app.route("/read")
def read_data():
    f = open("status.json","r")
    data = f.read()
    f.close()
    return data
  
@app.route("/")
def index():
    return render_template('index.html')
#Phils Stuff
def analyse(data):
    print(data)
    if(data["status"]):
        print("anschatlen")
    else:
        print("ausschalten")



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)