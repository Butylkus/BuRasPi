#!/usr/bin/python3.4
#coding=utf-8
#Скрипт для подписчиков канала http://www.youtube.com/user/butylkus
#Лицензия GPL v2
#Автор: Алексей Butylkus, https://vk.com/butpub

#Импортируем модули и настраиваемся
import RPi.GPIO as GPIO
import time, os
script_version = "0.1"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#переменные очевидны...
relay1 = 6 
relay2 = 13
relay3 = 14
relay4 = 15
relay5 = 16 
relay6 = 19
relay7 = 26 
relay8 = 2  


#инициализация - гасим все огни
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)
GPIO.setup(relay5, GPIO.OUT)
GPIO.setup(relay6, GPIO.OUT)
GPIO.setup(relay7, GPIO.OUT)
GPIO.setup(relay8, GPIO.OUT)

GPIO.output(relay1, 1)
GPIO.output(relay2, 1)
GPIO.output(relay3, 1)
GPIO.output(relay4, 1)
GPIO.output(relay5, 1)
GPIO.output(relay6, 1)
GPIO.output(relay7, 1)
GPIO.output(relay8, 1)

os.system("clear")

print("Программа теста 8-канального модуля реле\nКаждое реле включается по очереди\nВведите число согласно инструкции:")

rounds = int(input("\t[ЧИСЛО] - Количество проходов\n\t0 - выход\nВаш ввод: "))

if rounds > 0:
    for i in range (1, rounds):
        print("Реле 1 на пине", relay1)
        GPIO.output(relay1, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay1, 1)
        time.sleep(0.1)

        print("Реле 2 на пине", relay2)
        GPIO.output(relay2, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay2, 1)
        time.sleep(0.1)

        print("Реле 3 на пине", relay3)
        GPIO.output(relay3, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay3, 1)
        time.sleep(0.1)

        print("Реле 4 на пине", relay4)
        GPIO.output(relay4, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay4, 1)
        time.sleep(0.1)

        print("Реле 5 на пине", relay5)
        GPIO.output(relay5, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay5, 1)
        time.sleep(0.1)

        print("Реле 6 на пине", relay6)
        GPIO.output(relay6, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay6, 1)
        time.sleep(0.1)

        print("Реле 7 на пине", relay7)
        GPIO.output(relay7, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay7, 1)
        time.sleep(0.1)

        print("Реле 8 на пине", relay8)
        GPIO.output(relay8, 0)
        time.sleep(1.25)
        os.system("clear")
        GPIO.output(relay8, 1)
        time.sleep(0.1)


os.system("clear")
print("Спасибо за пользование программой!\nХорошего дня и ПОДПИШИСЬ НА КАНАЛ ;)\n\t\t>>>>http://www.youtube.com/user/butylkus<<<<")
GPIO.cleanup() #Прибираемся
