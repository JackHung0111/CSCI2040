# 1155108381 1155110154 
# lab 2 p1

def check_sublist(list1, d1, d2):
    lista = []
    listb = []
    listc = []
    for integer in list1:
        if (integer > d1 * d2):
            lista.append(integer)
        if (integer < d1 * d2):
            listb.append(integer)
        if (integer < d1 or integer < d2):
            listc.append(integer)
    return lista, listb, listc

# print(check_sublist([21, 25, 4, 6, 28], 3, 7))