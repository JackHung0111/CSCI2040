import getpass

ans = int(getpass.getpass(prompt = "Player 1, write down your number secretly: "))
while (ans < -100 or ans > 100):
    ans = int(getpass.getpass(prompt = "Player 1, invalid input, write down your number secretly: "))

trying = 0
correct = False

while (trying <= 6 and correct == False):
    guess = int(input("Player 2, input your guess: "))
    trying = trying + 1
    if (guess < ans):
        print("Your guess is too low!")
    elif (guess > ans):
        print("Your guess is too high!")
    else:
        print("You are right after trying for", trying,"times.Program ends.")
        correct = True
if (trying == 7 and correct == False):
    print("You have tried 6 times and it is still wrong!The answer is", ans, "and program ends.")