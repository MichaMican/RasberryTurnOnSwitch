from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
import RPi.GPIO as GPIO

LastStatus = False
statusJSONFile = "./IO/currentStatus.json"

#check if server is turned on or off
def check_status():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.IN)
    while True:

        status = {}

        print(GPIO.INPUT)

        if GPIO.INPUT == 1:
            print("server an")
            status["status"] = True
        else:
            print("server aus")
            status["status"] = False
        
        if status["status"] != LastStatus:
            LastStatus = status["status"]
            with open(statusJSONFile, 'w') as f:
                f.write(json.dumps(status))
    
