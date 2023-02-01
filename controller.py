
import find_name
import view
import model_menu
# from tkinter import *
# from tkinter import ttk
# frm = None


def select():
    view.input_otvet()
    otvet = int(input())
    model_menu.select(otvet)


def friend_name():
    view.creat_menu_name()
    find_name.find()


# def click_button_find():
#     model_menu.click_find()


# def click_button_new_date():
#     model_menu.click_new_date()


# def click_button_list():
#     model_menu.click_list()


# def click_button_import():
#     model_menu.click_import


def start():
    view.creat_menu()
    select()
    # global frm

    # root = Tk()
    # frm = ttk.Frame(root, padding=30)
    # frm.grid()
    # name_prog = ttk.Label(frm, text='Справочник чайника')
    # name_prog.grid(row=0, column=1)

    # button_find = ttk.Button(
    #     frm, text='1. Найти телефон друга', command=click_button_find)
    # button_find.grid(row=1, column=1)

    # button_new_date = ttk.Button(
    #     frm, text='2. Записать нового друга', command=click_button_new_date)
    # button_new_date.grid(row=2, column=1)

    # button_list = ttk.Button(
    #     frm, text='3. Вывести список контактов', command=click_button_list)
    # button_list.grid(row=3, column=1)

    # button_import = ttk.Button(
    #     frm, text='4. Импорт контактов', command=click_button_import)
    # button_import.grid(row=4, column=1)

    # ttk.Button(frm, text='Выход').grid(row=6, column=2)

    # lable_vivod = ttk.Label(frm, text='Вывод: ')
    # lable_vivod.grid(row=5, column=1)

    # root.mainloop()
