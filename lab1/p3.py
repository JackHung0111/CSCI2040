x = []
s = ""

unit_GPA = 0.0
credit_GPA = 0.0
unit_mGPA = 0.0
credit_mGPA = 0.0

while(s != "-1"):
    s = input()
    x = s.split(" ")
    while((float(x[0]) < 0 or float(x[0]) > 5.0 or int(x[1]) <= 0) and s != "-1"):
        print("Wrong input!")
        s = input()
        x = s.split(" ")
    if(s != "-1"):
        unit_GPA = unit_GPA + float(x[0]) * int(x[1])
        credit_GPA = credit_GPA + int(x[1])
        if(int(x[2]) == 1):
            unit_mGPA = unit_mGPA + float(x[0]) * int(x[1])
            credit_mGPA = credit_mGPA + int(x[1])
        print("Current GPA: ", "{0:.2f}".format(unit_GPA / credit_GPA))
        if(credit_mGPA == 0):
            print("Current major GPA: 0.00")
        else:
            print("Current major GPA: ", "{0:.2f}".format(unit_mGPA / credit_mGPA))
print("Program ends.")
