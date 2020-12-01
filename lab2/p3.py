# 1155108381 1155110154 
# lab 2 p3

def fibo(x1, x2):

    value = x1 + x2

    if (value <= 1000):
        value = fibo(x2,value)

    return value

# print(fibo(1,1))