print("...Rock...")
print("...Paper...")
print("...Scissors...\n")

# Take inputs and check if users input the right thing
print("Enter player 1's choice: ")
player_1 = input()
player_1 = player_1.lower()
if player_1 != "rock" and player_1 != "paper" and player_1 != "scissors":
    print("Input Error!")
    quit()

print("Enter player 2's choice: ")
player_2 = input()
player_2 = player_2.lower()
if player_2 != "rock" and player_2 != "paper" and player_2 != "scissors":
    print("Input Error!")
    quit()

# Check who is the winner
if player_1 == player_2:
    print("SHOOT!")
    print("It is a tie!")
elif player_1 == "rock":
    if player_2 == "paper":
        print("SHOOT!")
        print("player 2 wins!")
    elif player_2 == "scissors":
        print("SHOOT!")
        print("player 1 wins!")
elif player_1 == "paper":
    if player_2 == "scissors":
        print("SHOOT!")
        print("player 2 wins!")
    elif player_2 == "rock":
        print("SHOOT!")
        print("player 1 wins!")
else:
    if player_2 == "rock":
        print("SHOOT!")
        print("player 2 wins!")
    elif player_2 == "paper":
        print("SHOOT!")
        print("player 1 wins!")
