# 1155108381 1155110154 
# lab 4 p1

import math

a = [n for n in range(1,11)]

# A list of round down square root of the corresponding values in the original list
result1 = list(map(lambda n: math.floor(math.sqrt(n)), a))

# A list where each element is larger by one than the corresponding element in the original list
result2 = list(map(lambda n: n + 1, a))

# A list contains values in the original list that are less than or equal to 7
result3 = [n for n in a if n <= 7]

# A list contains values that are the square of odd values in the original list
result4 = [n*n for n in a if n%2 != 0]
