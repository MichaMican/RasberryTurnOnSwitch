from flask import Flask, request, render_template
from flask_cors import CORS
import json
import time
import datetime
import os
import RPi.GPIO as GPIO


LastStatus = ''
statusJSONFile = "./IO/currentstatus.json"

#check if server is turned on or off
def check_status():
    global LastStatus
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.IN)
    while True:
        if GPIO.INPUT == 1:
            print("server an")
            LastStatus = '{"Status":true}'
        else:
            print("server aus")
            LastStatus = '{"Status":false}'
