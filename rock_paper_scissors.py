print("...Rock...")
print("...Paper...")
print("...Scissors...\n")

# Take inputs and check if users input the right thing
print("Enter player 1's choice: ")
player_1 = input()
if player_1 != "Rock" and player_1 != "Paper" and player_1 != "Scissors":
    print("Input Error!")
    quit()

print("Enter player 2's choice: ")
player_2 = input()
if player_2 != "Rock" and player_2 != "Paper" and player_2 != "Scissors":
    print("Input Error!")
    quit()

# Check who is the winner
if player_1 == player_2:
    print("SHOOT!")
    print("It is a tie!")
elif player_1 == "Rock":
    if player_2 == "Paper":
        print("SHOOT!")
        print("player 2 wins!")
    elif player_2 == "Scissors":
        print("SHOOT!")
        print("player 1 wins!")
elif player_1 == "Paper":
    if player_2 == "Scissors":
        print("SHOOT!")
        print("player 2 wins!")
    elif player_2 == "Rock":
        print("SHOOT!")
        print("player 1 wins!")
else:
    if player_2 == "Rock":
        print("SHOOT!")
        print("player 2 wins!")
    elif player_2 == "Paper":
        print("SHOOT!")
        print("player 1 wins!")
