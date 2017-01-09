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
relay1 = 2

#инициализация - Настраиваем вывод
GPIO.setup(relay1, GPIO.OUT)

#инициализация - отключаем реле, если было включено
GPIO.output(relay1, 1)


os.system("clear")

print("Программа управления водяной помпой\nПомпа включается и выключается по команде\n")

cmd = int(input("\t1 - вкл\n\t2 - выкл\n\t0 - выход\nКоманда:"))

while cmd!=0:
    if cmd==1:
        os.system("clear")
        print("Твоя помпа сосёт!")
        GPIO.output(relay1, 0)
        cmd = int(input("\t1 - вкл\n\t2 - выкл\n\t0 - выход\nКоманда:"))
    
    if cmd==2:
        os.system("clear")
        print("И тишина...")
        GPIO.output(relay1, 1)
        cmd = int(input("\t1 - вкл\n\t2 - выкл\n\t0 - выход\nКоманда:"))



#Прибираемся
os.system("clear")
print("Спасибо за пользование программой!\nХорошего дня и ПОДПИШИСЬ НА КАНАЛ ;)\n\t\t>>>>http://www.youtube.com/user/butylkus<<<<")
GPIO.cleanup()
