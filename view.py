import find_name
import dic


def creat_menu():
    print('1. Найти телефон друга ')
    print('2. Записать нового друга ')
    print('3. Вывести список контактов ')


def input_otvet():
    print('Введи необходимы пункт: ')


def creat_menu_name():
    print('Введи необходимое имя: ')


def print_name_friend(name):
    print('{} {}'.format(name, dic.dicion[name]))


def print_new_name_friend(new_name):
    print('{} {}'.format(new_name, dic.dicion[new_name]))


def otvet_net_new(name):
    print('Занести друга в справочник?')


def otvet_net_i_ne_nada(name):
    print('Ok')


def otvet_zapic():
    print('Вывести новый список?')


def print_spisok():
    print(dic.dicion)


def otvet_net():
    print('Ok')
