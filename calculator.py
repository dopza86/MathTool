def add(*args):
    result = 0
    list_args = list(args)
    for i in list_args:
        result = i + result
    return result


def substract(*args):

    substract_num = 0
    list_args = list(args)
    for j in list_args:
        substract_num = substract_num - j

    return substract_num + (list_args[0]) * 2


print(add(3, 5, 10, 15))
