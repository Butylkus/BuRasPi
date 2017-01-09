#!/usr/bin/python3
#Лицензия GPL v2

import time
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(21, GPIO.FALLING, bouncetime=100)



def check_button():
    print ("=========КНОПУЛЕЧКА!=========")

try:
    while True:
        print(datetime.strftime(datetime.now(), "%M:%S"))
        time.sleep(0.1)
        if GPIO.event_detected(21):
            check_button()
