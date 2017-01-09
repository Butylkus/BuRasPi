#!/usr/bin/python3.4
#coding=utf-8
#Скрипт для подписчиков канала http://www.youtube.com/user/butylkus
#Лицензия GPL v2
#Автор: Алексей Butylkus, https://vk.com/butpub

import time, math

lower=int(input("\nНачало диапазона: "))
upper=int(input("Конец диапазона: "))

primalcounter=0

print("Поехали! =)\n")
starttime = int(time.time())
for current in range(lower,upper+1):
    iterator=2
    delitelej=0
    while iterator<=round(math.sqrt(current)):
        if not current%iterator:
            delitelej=delitelej+1
        iterator=iterator+1
    if delitelej==0:
        estimated = int(time.time()) - starttime
        print (current, ": спустя", estimated, "секунд от старта")
        primalcounter = primalcounter+1
        
        
estimated = int(time.time()) - starttime
print ("Мы закончили вычисления.\nВсего в диапазоне",lower,"-",upper,"нашлось",primalcounter,"простых чисел.\nВремени убито:", estimated, "секунд")
