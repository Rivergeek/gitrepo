import os
import sys
import psutil   #сторонний модуль
import shutil

def sys_info():
    print('Вот что я знаю о системе:')
    print('Все текущие процессы: ', psutil.pids())
    print('Количество ядер процессора: ', psutil.cpu_count())
    print('Платформа: ', sys.platform)
    print('Кодировка файловой системы: ', sys.getfilesystemencoding())
def ydalit():
    print('Удаление дубликатов в директории')
    dirname = input('Укажите имя директории:')
    a = int(len(os.listdir(dirname)))
    file_list = os.listdir(dirname)
    i = 0
    # while i < len(file_list):
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
    b = int(len(os.listdir(dirname)))
    c = a - b
    print('Файлов удалено: ', c)



name = input("Введите_имя: ")
print('Привет ' + name + '!')

quest = ""
while quest != "q":
    quest = input("Поработаем? (д/н/q) : ")
    if quest == "д":
        print('Что будем делать?')
        print('1 - Вывести список файлов')
        print('2 - Вывести информацию о системе')
        print('3 - Номер текущего процесса')
        print('4 - Продублировать файлы в текущей директории')
        print('5 - Удалить дубликаты')
        deis = int(input("Укажите номер действи: "))
        if deis == 1:
            print(os.listdir())
        elif deis == 2:
            sys_info()
        elif deis == 3:
            print(os.getpid())
        elif deis == 4:
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]):
                    newfile = file_list[i] + '.dupl'
                    shutil.copy(file_list[i], newfile)   #копирование
                    if os.path.exists(newfile):       # функцая возвращает значение TRUE если файл есть
                        print('Файл ', newfile, ' был успешно создан')
                    else:
                        print('Возникли проблемы копирования')
                i += 1
        elif deis == 5:
            ydalit()
                #i += 1
        else:
            pass
    elif quest == "н":
        print('РАБОТАЙ!')
    else:
        print('Лентяй!')

