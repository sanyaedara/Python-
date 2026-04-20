import random

choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)

you = input("Enter your choice:")
print(f"You chose {you}")
print(f"Computer chose {computer}")

if you not in choices:
    print("Invalid input")
elif computer == you:
    print("It's a draw")
elif((computer == "rock" and you == "paper") or
    (computer == "paper" and you == "scissor") or
    (computer == "scissor" and you == "rock")):
    print("You win!!")
else:
    print("Computer won. Better luck next time...")
