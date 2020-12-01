str1 = input("Please input the first number:")
while (str1.replace('.', '', 1).replace('-', '', 1).isdigit() != True):
    print("Your input is not a number!")
    str1 = input("Please input the first number:")
if (str1.find('.') < 0):
    num1 = int(str1)
else:
    num1 = float(str1)

str2 = input("Please input the second number:")
while (str2.replace('.', '', 1).replace('-', '', 1).isdigit() != True):
    print("Your input is not a number!")
    str2 = input("Please input the second number:")
if (str2.find('.') < 0):
    num2 = int(str2)
else:
    num2 = float(str2)

str3 = input("Please input the third number:")
while (str3.replace('.', '', 1).replace('-', '', 1).isdigit() != True):
    print("Your input is not a number!")
    str3 = input("Please input the third number:")
if (str3.find('.') < 0):
    num3 = int(str3)
else:
    num3 = float(str3)

str4 = input("Please input the fourth number:")
while (str4.replace('.', '', 1).replace('-', '', 1).isdigit() != True):
    print("Your input is not a number!")
    str4 = input("Please input the fourth number:")
if (str4.find('.') < 0):
    num4 = int(str4)
else:
    num4 = float(str4)

list1 = [num1,num2,num3,num4]
list1.sort()
print("The second smallest value is", list1[1])
print("The second biggest value is", list1[2])
print("Program ends.")

