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
relay1 = 2 
relay2 = 3
relay3 = 4
relay4 = 14
butlight = 22
button = 21


#инициализация - гасим все огни
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)
GPIO.setup(butlight, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(relay1, 1)
GPIO.output(relay2, 1)
GPIO.output(relay3, 1)
GPIO.output(relay4, 1)
GPIO.output(butlight, 0)

os.system("clear")

print("Программа управления блоком из 4 реле\nОдиночное нажатие включает случайную комбинацию\nДесятое нажатие отключает весь блок и завершает программу")

poweroff=0

while poweroff<10:
    if GPIO.input(21) == False:
        GPIO.output(butlight, 1)
        GPIO.output(relay1, random.randint(0, 1))
        GPIO.output(relay2, random.randint(0, 1))
        GPIO.output(relay3, random.randint(0, 1))
        GPIO.output(relay4, random.randint(0, 1))
        poweroff = poweroff+1
        print ("Нажатие №",poweroff, sep="")
        time.sleep(0.5)
        GPIO.output(butlight, 0)

os.system("clear")
print ("Программа насчитала 10 нажатий и будет завершена через 10 секунд!",poweroff, sep="")
time.sleep(10)

os.system("clear")
print("Спасибо за пользование программой!\nХорошего дня и ПОДПИШИСЬ НА КАНАЛ ;)\n\t\t>>>>http://www.youtube.com/user/butylkus<<<<")
GPIO.cleanup() #Прибираемся
