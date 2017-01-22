#!/usr/bin/python3
#coding=utf-8
#Лицензия GPL v3
#Автор: Алексей Butylkus, https://vk.com/butpub, https://www.youtube.com/user/butylkus

import os, sys, time
import Adafruit_DHT as dht
from datetime import datetime

sensor = 11
pin = 14

while True:
    humidity, temperature = dht.read_retry(sensor, pin)
    if (humidity is not None) and (temperature is not None):
        nowtime = datetime.strftime(datetime.now(), "%d.%m %H:%M:%S")
        temperature = str(temperature)
        humidity = str(humidity)
        print(nowtime + "\t" + temperature + "C\t" + humidity +"%")
        time.sleep(3)

