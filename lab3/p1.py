# 1155108381 1155110154 
# lab 3 p1

def non_unique(list):
    result = []
    for char in list:
        count = list.count(char)
        if (count > 1):
            result.append(char)
            result.append(count)
            while(list.count(char) > 0):
                list.remove(char)
    return result

