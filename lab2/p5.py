# 1155108381 1155110154 
# lab 2 p5

def count_alphabet(test_string):
    count = 0
    for char in test_string:
        if (char.isalpha()):
            count += 1
    return count

def vowel_capitalization(test_string):
    str1 = test_string
    str1 = str1.replace('a','A')
    str1 = str1.replace('e','E')
    str1 = str1.replace('i','I')
    str1 = str1.replace('o','O')
    str1 = str1.replace('u','U')    
    return str1

def concat(test_string, new_string):
    return test_string + new_string

def search(test_string, sub):
    return test_string.rfind(sub)

def letter_count(test_string):
    str1 = test_string.lower()
    list1 = []
    for i in range(97,123):
        count = str1.count(chr(i))
        if (count > 0):
            list1.append((chr(i), count))
    return list1

"""
s = "Alice was born in 1996 and born in London. She is 22 now."
print(count_alphabet(s))
print(vowel_capitalization(s))
print(concat(s,"TEST"))
print(search(s,"in"))
print(letter_count(s))
"""
