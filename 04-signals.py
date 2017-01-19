#!/usr/bin/python3
#coding=utf-8
#Лицензия GPL v3
#Автор: Алексей Butylkus, https://vk.com/butpub, https://www.youtube.com/user/butylkus

import signal, sys, os
from datetime import datetime

def daemon_stop(signum, frame):
    sys.exit("Спасибо за пользование программой!\nХорошего дня и ПОДПИШИСЬ НА КАНАЛ ;)\n\t\t>>>>http://www.youtube.com/user/butylkus<<<<")

signal.signal(signal.SIGTERM, daemon_stop)

while True:
    print(datetime.strftime(datetime.now(), "%H:%M:%S") + " - работаем...")
    os.system('clear')
  

