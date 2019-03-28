from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
import RPi.GPIO as GPIO

lastStatus = False
statusJSONFile = "./IO/currentStatus.json"

#check if server is turned on or off
def checkStatus():
    global lastStatus
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.IN)
    while True:

        status = {}

        print(GPIO.input(15))

        if GPIO.input(15) == 1:
            print("server an")
            status["status"] = True
        else:
            print("server aus")
            status["status"] = False
            
        print(status["status"])
        
        if status["status"] != lastStatus:
            print("UPDATED!")
            status["lastChanged"] = datetime.datetime.now()
            lastStatus = status["status"]
            with open(statusJSONFile, 'w') as f:
                f.write(json.dumps(status))
                
        time.sleep(1)
    
if __name__ == '__main__':
    checkStatus()