# 1155108381 1155110154 
# lab 2 p2

def roman_to_decimal(str):
    n = 0
    str1 = str
    if("-" in str1):
        return -1
    n += str1.count("IV") * 4
    str1 = str1.replace("IV","")
    n += str1.count("IX") * 9
    str1 = str1.replace("IX","")
    n += str1.count("XL") * 40
    str1 = str1.replace("XL","")
    n += str1.count("XC") * 90
    str1 = str1.replace("XC","")
    n += str1.count("CD") * 400
    str1 = str1.replace("CD","")
    n += str1.count("CM") * 900
    str1 = str1.replace("CM","")
    n += str1.count('I') + str1.count('V')  * 5 + str1.count('X') * 10
    n += str1.count('L') * 50 + str1.count('C')  * 100 + str1.count('D') * 500 + str1.count('M') * 1000
    if(n > 9999):
        return -1 
    return n

# print(roman_to_decimal("MMMMMMMDCCLXVI"))