# 여러인자를 받는 계산기


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


def multiply(*args):
    list_args = list(args)
    multiply_num = 1
    for k in list_args:
        multiply_num = multiply_num * k
    return multiply_num


def devide(*args):
    list_args = list(args)
    devide_num = 1
    for l in list_args:
        devide_num = devide_num / l
    return devide_num * (list_args[0] ** 2)
