# 1155108381 1155110154 
# lab 4 p2

from functools import reduce

def low_freq_word_count(x, str, n, m):
    a = list(filter(lambda b: (b.count(str) < m and b.count(str)>0 and len(b) > n), x))
    # print(a)
    b = [1 for n in a]
    # print(b)
    if(len(b) > 0):
        return reduce(lambda x,y: x+y,b)
    else:
        return 0
"""
print(
    low_freq_word_count
    (['python is boring',
            'pythom is a large heavy-bodied snake',
            'The python course is worse taking',
            'The python course is worth taking',
            'python python python python'], 'python', 20, 3)
)"""