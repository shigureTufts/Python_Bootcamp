import random

print("...Rock...")
print("...Paper...")
print("...Scissors...\n")

# create a list of choice for AI to choose
choice_list = ["Rock", "Paper", "Scissors"]
ai = random.randint(0, 2)

# take in user input
print("Enter your choice:")
player = input()
player = player.lower()

# transform AI choice into strings
if ai == 0:
    ai = "rock"
elif ai == 1:
    ai = "paper"
else:
    ai = "scissors"

# copy wining logic from two players mode
if player == ai:
    print("SHOOT!")
    print("It is a tie!")
elif player == "rock":
    if ai == "paper":
        print("SHOOT!")
        print("AI wins!")
    elif ai == "scissors":
        print("SHOOT!")
        print("Player wins!")
elif player == "paper":
    if ai == "scissors":
        print("SHOOT!")
        print("AI wins!")
    elif ai == "rock":
        print("SHOOT!")
        print("Player wins!")
else:
    if ai == "rock":
        print("SHOOT!")
        print("AI wins!")
    elif ai == "paper":
        print("SHOOT!")
        print("Player wins!")
