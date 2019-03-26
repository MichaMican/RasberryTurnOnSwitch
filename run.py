from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
import RPi.GPIO as GPIO


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

@app.route("/notAus", methods=['POST'])
def notAus():
    foo = data

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
    if(data["status"]):
        print("anschalten")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(16, GPIO.LOW)
    else:
        print("ausschalten")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(16, GPIO.LOW)

    #is needed to reset the status of any GPIO pins when you exit the programm
    GPIO.cleanup()


if __name__ == '__main__':
    app.run(host='192.168.0.44', port=5321, debug=True)   