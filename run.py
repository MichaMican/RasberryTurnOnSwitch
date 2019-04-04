from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
import RPi.GPIO as GPIO


app = Flask(__name__)
CORS(app)

currentStatusJSONFile = "./IO/currentStatus.json"
statusJSONFile = "./IO/status.json"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)


#Webserver Stuff
@app.route("/write", methods=['POST'])
def write_data():
    data = request.get_json()
    with open(statusJSONFile, 'w') as f:
        f.write(json.dumps(data))
    analyse(data)
    return "OK"

@app.route("/notAus", methods=['POST'])
def notAus():
    data = request.json()

@app.route("/read")
def read_data():
    data = ''
    with open(statusJSONFile, 'r') as f:
        data = f.read()
    return data

@app.route("/")
def index():

    global currentStatusJSONFile
    global statusJSONFile

    currentStatusString = ''
    statusString = ''

    #Sync status with currentStatus
    with open(currentStatusJSONFile, 'r') as f:
        currentStatusString = f.read()

    with open(statusJSONFile, 'r') as f:
        statusString = f.read()

    currentStatusJSON = json.loads(currentStatusString)
    statusJSON = json.loads(statusString)

    print(currentStatusJSON["status"])
    print(currentStatusJSON["lastChanged"])

    convertedDateTime = datetime.datetime.strptime(currentStatusJSON["lastChanged"], '%Y-%m-%d %H:%M:%S.%f')
    timeDifference = (datetime.datetime.now() - convertedDateTime).total_seconds
    
    print("Seconds since last state change: " + str(timeDifference))

    if currentStatusJSON["status"] != statusJSON["status"] and timeDifference > 5:
        statusJSON["status"] = currentStatusJSON["status"]
        with open(statusJSONFile, 'w') as f:
            f.write(json.dumps(statusJSON))

    return render_template('index.html')


#Turning px on/off
def analyse(data):

    global currentStatusJSONFile

    currentStatus = ''
    
    with open(currentStatusJSONFile, 'r') as f:
        currentStatus = f.read()

    if (data["status"] != currentStatus["status"]):
        if(data["status"]):
            print("anschalten")
            GPIO.output(16, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(16, GPIO.LOW)
        else:
            print("ausschalten")
            GPIO.output(16, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(16, GPIO.LOW)
    else:
        print("The PC is already in this State!")



if __name__ == '__main__':
    app.run(host='192.168.0.44', port=61234, debug=True)   