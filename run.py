from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
import RPi.GPIO as GPIO


#setup GPIO using Board numbering + Pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
app = Flask(__name__)
CORS(app)


statusJSONFile = "./IO/status.json"

@app.route("/write", methods=['POST'])
def write_data():
    data = request.get_json()
    with open(statusJSONFile, 'w') as f:
        f.write(json.dumps(data))
    analyse(data)
    return "OK"

@app.route("/read")
def read_data():
    data = ''
    with open(statusJSONFile, 'r') as f:
        data = f.read()
    return data

@app.route("/")
def index():
    return render_template('index.html')

#Phils Stuff

#turning on/off the Server with help of internet
def analyse(data):
    if(data.status):
        print("anschalten")
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(16, GPIO.LOW)
    else:
        print("ausschalten")
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(16, GPIO.LOW)

    #is needed to reset the status of any GPIO pins when you exit the programm
    GPIO.cleanup()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)   
