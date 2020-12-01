# 1155108381 1155110154 
# lab 3 p2

def quicksort(a):
    result = []
    if (a != []):
        pivot = a[0]
        less = quicksort([x for x in a[1:] if x < pivot])
        great = quicksort([x for x in a[1:] if x >= pivot])
        return less + [pivot] + great
    return result 
