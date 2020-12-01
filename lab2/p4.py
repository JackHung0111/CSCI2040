# 1155108381 1155110154 
# lab 2 p4

import math

def check_invalid(triangle):
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    if (a > 0 and b > 0 and c > 0):
        if (a + b > c or a + c > b or c + b > a):
            return False
    return True

def is_isosceles_triangle(triangle):
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    if (check_invalid(triangle) != True):
        if (a == b or c == a or b == c):
            return True
    return False

def perimeter(triangle):
    n = 0
    for side in triangle:
        n += side
    return n

def area(triangle):
    s = perimeter(triangle) / 2.0
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

"""
T1 = (10, 10, 8)
print(check_invalid(T1))
print(is_isosceles_triangle(T1))
print(perimeter(T1))
print(area(T1))
"""