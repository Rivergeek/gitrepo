import os
import sys
import psutil          #сторонний модуль

name = input("Введите_имя: ")
print('Привет ' + name + '!')
quest = input("Поработаем? (д/н) : ")
if quest == "д":
    print('Что будем делать?')
    print('1 - Вывести список файлов')
    print('2 - Вывести информацию о системе')
    print('3 - Номер текущего процесса')
    deis = int(input("Укажите номер действи: "))
    if deis == 1:
        print(os.listdir())
    elif deis == 2:
        print(psutil.pids())
    elif deis == 3:
        print(os.getpid())
    else:
        pass
elif quest == "н":
    print('Пока')
else:
    print('Лентяй!')
