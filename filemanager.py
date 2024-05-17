from victory import victory
from use_functions import bankfunc
from listdir import listdir
import os
import shutil

while True:
    print('1 - Создать папку\t\t\t\t', ' 8 - Просмотр информации об ОС')
    print('2 - Удалить файл/папку\t\t\t', ' 9 - Создатель программы')
    print('3 - Копировать файл/папку\t\t', ' 10 - Играть в викторину')
    print('4 - Просмотр рабочей директории\t', '11 - Мой банковский счёт')
    print('5 - Просмотреть только папки\t', '12 - Смена рабочей директории')
    print('6 - Просмотреть только файлы\t', '13 - Выход')
    print('7 - Сохранить содержимое рабочей директории в файл')
    print()
    choice = input('Выберите пункт меню: ')
    if choice == '1':  # Done
        folder = input('Введите название папки: ')
        if not os.path.exists(folder):
            os.mkdir(folder)
        print()
    elif choice == '2':  # Done
        rm = input('Что хотите удалить, файл (f) или папку (d)? ')
        if rm == 'f':
            os.remove(input('Введите название файла: '))
        elif rm == 'd':
            shutil.rmtree(input('Введите название папки: '))
        else:
            print('Непонятно, что нужно удалить.')
        print()
    elif choice == '3':
        print()
        cp = input('Что хотите скопировать, файл (f) или папку (d)? ')
        print()
        if cp == 'f':
            src = input('Введите название файла, который нужно скопировать: ')
            dst = input('Введите новое название файла: ')
            shutil.copy(src, dst)
        elif cp == 'd':
            src = input('Введите название папки, которую нужно скопировать: ')
            dst = input('Введите новое название папки: ')
            shutil.copytree(src, dst)
        else:
            print('Непонятно, что нужно скопировать.')
        print()
    elif choice == '4':  # Done
        print()
        print('Содержимое рабочей директории:')
        print(sorted(os.listdir()))
        print()
    elif choice == '5':  # Done
        print()
        path = '.'
        print([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))])
        print()
    elif choice == '6':  # Done
        print()
        path = '.'
        print([x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))])
        print()
    elif choice == '7':
        listdir()
    elif choice == '8':  # Done
        print()
        print(os.uname())
        print()
    elif choice == '9':  # Done
        print()
        print('Создатель программы: Ярослав С. Васильев,')
        print('студент Университета ИИ (2023)')
        print()
    elif choice == '10':  # Done
        victory()
    elif choice == '11':  # Done
        print()
        bankfunc()
    elif choice == '12':  # Done
        print()
        os.chdir(input('Введите путь к новой рабочей директории: '))
        print('Новая рабочая директория:')
        print(os.getcwd())
        print()
    elif choice == '13':  # Done
        break
    else:
        print('Неверный пункт меню')
        print()
