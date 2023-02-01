import dic
import new_date
import view
import controller


def find():
    name = input()
    if name in dic.dicion:
        view.print_name_friend(name)
        controller.start()
    elif name not in dic.dicion:
        view.otvet_net_new(name)
        otvet = input()
        if otvet == "да":
            new_date.zapis_date()
        elif otvet == "нет":
            view.otvet_net_i_ne_nada(name)
