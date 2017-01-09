#!/usr/bin/python3.4
#coding=utf-8
#Лицензия GPL v2

import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(21)
    if input_state == False:
        print('Кнопка!')
        os.system("clear") 

