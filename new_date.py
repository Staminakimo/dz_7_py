import dic
import view


def zapis_date():
    new_name = input('Введите имя друга: ')
    new_name_phone = input('Введите номер друга: ')
    dic.dicion[new_name] = new_name_phone
    view.otvet_zapic()
    otvet = input()
    if otvet == "да":
        view.print_spisok()
    else:
        view.otvet_net()
