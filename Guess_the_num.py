import random
num = random.randint(1,100)
guess = 0
a = -1

while(a!=num):
    guess += 1
    a = int(input("Enter your guess: "))
    if (a>num):
        print("Lower number please")
    else:
        print("Higher number please")
print(f"You have guessed the number {num} in {guess} guesses")
