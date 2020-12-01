s1 = input("Please input a palindrome: ")

palindrome = False

while(palindrome == False):
    s1 = s1.replace(" ","")
    s2 = s1[::-1]
    if(s1 != s2):
        s1 = input("No, you must input a palindrome: ")
    else:
        palindrome = True
else:
    print("Welcome to the wonderland!")