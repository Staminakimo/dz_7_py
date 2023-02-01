import controller
import new_date
import view
import find_name


def select(otvet):
    if otvet == 1:
        controller.friend_name()
    if otvet == 2:
        new_date.zapis_date()
    if otvet == 3:
        view.print_spisok()


def click_find():
    find_name.find()


def click_new_date():
    new_date.zapis_date()


def click_list():
    view.print_spisok()


def click_import():
    print('пока нет')
