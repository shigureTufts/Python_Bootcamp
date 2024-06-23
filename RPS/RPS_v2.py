import random

player_wins = 0
ai_wins = 0
winning_score = 3
while player_wins < winning_score and ai_wins < winning_score:
    print(f"Player Score: {player_wins}     AI Score: {ai_wins}")
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
    if player == "quit" or player == "q":
        break

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
            ai_wins += 1
        elif ai == "scissors":
            print("SHOOT!")
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if ai == "scissors":
            print("SHOOT!")
            print("AI wins!")
            ai_wins += 1
        elif ai == "rock":
            print("SHOOT!")
            print("Player wins!")
            player_wins += 1
    else:
        if ai == "rock":
            print("SHOOT!")
            print("AI wins!")
            ai_wins += 1
        elif ai == "paper":
            print("SHOOT!")
            print("Player wins!")
            player_wins += 1

print(f"Final score: Player Score: {player_wins}     AI Score: {ai_wins}")
if player_wins < ai_wins:
    print("AI won the game!")
elif player_wins == ai_wins:
    print("It is a tie!")
else:
    print("Player won the game!")