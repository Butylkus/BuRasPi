#!/usr/bin/python3
#coding=utf-8
#Лицензия GPL v3
#Автор: Алексей Butylkus, https://vk.com/butpub, https://www.youtube.com/user/butylkus


import RPi.GPIO as GPIO
import os, sys, time
from datetime import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #23 порт, входящий, стягивающий резистор

GPIO.add_event_detect(23, GPIO.RISING, bouncetime=2000) #детекция прерывания: 23 порт, подъём сигнала (с 0 на 1), "дребезг" игнорировать 2000 мсек


#Протокол тревоги - функция реакции на нарушителя. В данном случае просто пишет на экран сообщение
def alarm():
    print ("""
        =========ТРЕВОГА!=========
        """)


detected=0 #счётчик нарушителей/срабатываний

while detected < 10:
    print(datetime.strftime(datetime.now(), "%H:%M:%S") + " - всё тихо...")
    time.sleep(0.1)
    #Если происходит прерывание (подъём на 23 порту)
    if GPIO.event_detected(23):
        detected=detected+1 #считаем нарушителя
        alarm() #активируем протокол тревоги
        print("На " + datetime.strftime(datetime.now(), "%H:%M:%S") + "; поймано нарушителей: " + str(detected)) #Показываем счётчик нарушителей
        time.sleep(3) #ждём три секунды
    os.system("clear") #как бы риалтайм-интерактив =)


#завершение программы
#высвобождаем порты, прощаемся и выходим
GPIO.cleanup()
os.system("clear")
print("Десять нарушителей были пойманы нашим сенсором!")
print("Спасибо за пользование программой!\nХорошего дня и ПОДПИШИСЬ НА КАНАЛ ;)\n\t\t>>>>http://www.youtube.com/user/butylkus<<<<")
sys.exit()
