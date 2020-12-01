n = int(input("Enter an integer: "))
while (n > -1):
    s = input("Enter a string:")
    x = n - 1
    for i in range(0, n):
        for j in range(0, x):
            for k in range(0, len(s)):
                print(end = " ")
        x = x - 1
        for j in range(0, i+1):
            print(s, end = "")
        print()
    n = int(input("Enter an integer:"))
else:
    print("Program ends.")