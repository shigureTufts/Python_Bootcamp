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

# transform AI choice into strings
if ai == 0:
    ai = "Rock"
elif ai == 1:
    ai = "Paper"
else:
    ai = "Scissors"

# copy wining logic from two players mode
if player == ai:
    print("SHOOT!")
    print("It is a tie!")
elif player == "Rock":
    if ai == "Paper":
        print("SHOOT!")
        print("AI wins!")
    elif ai == "Scissors":
        print("SHOOT!")
        print("Player wins!")
elif player == "Paper":
    if ai == "Scissors":
        print("SHOOT!")
        print("AI wins!")
    elif ai == "Rock":
        print("SHOOT!")
        print("Player wins!")
else:
    if ai == "Rock":
        print("SHOOT!")
        print("AI wins!")
    elif ai == "Paper":
        print("SHOOT!")
        print("Player wins!")
