# 기본 계산기


def add(*args):
    add_num = 0
    list_args = list(args)
    for i in list_args:
        add_num = i + add_num
    return add_num


def substract(*args):
    substract_num = 0
    list_args = list(args)
    for j in list_args:
        substract_num = substract_num - j
    return substract_num + (list_args[0]) * 2
