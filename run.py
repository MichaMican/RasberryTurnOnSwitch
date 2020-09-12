from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
import time
import RPi.GPIO as GPIO

app = Flask(__name__)
CORS(app)

print("Reseting GPIOs")
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

print("Setting up Pins")

time.sleep(3)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

print("Finished Pin setup")


#Webserver Stuff
@app.route("/write", methods=['POST'])
def write_data():
    data = request.get_json()
    analyse(data)
    return "OK"

@app.route("/status")
def checkStatus():
    status = {}

    print(GPIO.input(15))

    if GPIO.input(15) == 1:
        print("server aus")
        status["status"] = False
    else:
        print("server an")
        status["status"] = True
        
    print(status["status"])

    return status
    

@app.route("/")
def index():
    return render_template('index.html')


#Turning pc on/off
def analyse(data):
    currentStatus= checkStatus()

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
    app.run(host='192.168.178.47', port=61772, debug=True)
