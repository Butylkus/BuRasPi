#!/usr/bin/python3.4
#coding=utf-8
#Скрипт для подписчиков канала http://www.youtube.com/user/butylkus
#Лицензия GPL v2
#Автор: Алексей Butylkus, https://vk.com/butpub

#Импортируем модули и настраиваемся
import RPi.GPIO as GPIO
import time, os, random
script_version = "0.1"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#переменные очевидны...
led1 = 2 
led2 = 4
led3 = 5
led4 = 13 

#инициализация - гасим все огни
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)
GPIO.output(led4, 0)



while True:
    
    #зажигаем случайные огни
    GPIO.output(led1, random.randint(0, 1))
    GPIO.output(led2, random.randint(0, 1))
    GPIO.output(led3, random.randint(0, 1))
    GPIO.output(led4, random.randint(0, 1))
    
    #ждём секунду
    time.sleep(0.2)
    
    #гасим огни перед новым циклом
    GPIO.output(led1, 0)
    GPIO.output(led2, 0)
    GPIO.output(led3, 0)
    GPIO.output(led4, 0)
