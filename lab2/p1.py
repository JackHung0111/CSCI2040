# 1155108381 1155110154 
# lab 2 p1

def check_sublist(list1, d1, d2):
    lista = [integer for integer in list1 if integer > d1*d2]
    listb = [integer for integer in list1 if integer < d1*d2]
    listc = [integer for integer in list1 if integer < d1 or integer < d2]

    return lista, listb, listc
