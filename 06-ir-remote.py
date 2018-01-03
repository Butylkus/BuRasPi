#!/usr/bin/python3
#coding=utf-8
#Лицензия GPL v3
#Автор: Алексей Butylkus, https://vk.com/butpub, https://www.youtube.com/user/butylkus
#Картинки взяты отсюда: http://www.oocities.org/wraithfivexwing/asciiart/asciisouthpark.txt

###############
## Для работы этого скрипта надо сначала установить модуль lirc: sudo apt install python3-lirc
## И надо иметь корректные настройки самого lircd, lircrc
## За подробностями: 
###############


import lirc


print("Данная программа демонстрирует работу lirc в связке с Python")

print("Подключаемся к lirc...")
socket = lirc.init("num")
print("Сокет: {0}".format(socket)) 

counter = 0
print("У тебя {0} очков. Набей сто очков, нажимая цифровые клавиши.".format(counter))


while (counter < 100):
    answer = lirc.nextcode()
    if (len(answer) > 0):
        counter = counter + int(answer[0])
        print ("Ты нажал {0}, твой счёт {1}".format(answer[0], str(counter)))

lirc.deinit()

print ("Отлично! Ты набил {0} очков, теперь я жду нажатия ОК для выхода".format(counter))

socket = lirc.init("control")
print("Сокет: {0}".format(socket))

key = ""
while (key != "OK"):
    answer = lirc.nextcode()
    if (len(answer) > 0):
        key = answer[0]
        if (key == "OK"):
            continue
        print ("ты нажал {0}, а я жду OK!".format(key))

lirc.deinit()

print ("""
                            __  _
                  .===.:  ""  ;=====..
              _.-'    _;_. __;     . `"_
            ,          ' 'r-]           -
          .'                             '.
         r^                                .
        r            __       _             \\
        L         .:"--.==.==.--":.         |
   .-==.'________//      |  |   `^C\_.---.__====
   |~   --------//    .-.|  | ,    ] .---""     "
   '            |\     "/ /\ \'    ] |          :
    \            \'...-_,'  '_'...-_-         .'
     '            '---        -----          ]'
      `-_..                                _-'
          \                 -             .'
           `.                           .'
             =.          --__.         -
               "-__                 _.'
                   =.             ." 
                     "-._        /  
                         -.   -.'  
                          [----]:
                        :'      '.
                       -'        |
                                  \
    
                    MMMMKAAAAAYYYY!!!!!
    """)
