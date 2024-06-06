import random

keep_playing = "y"
while keep_playing == "y":
    answer = random.randint(1, 10)
    user_guess = int(input("Guess a number between 1 to 10: "))
    while 1 > user_guess or 10 < user_guess:
        user_guess = int(input("Guess a number between 1 to 10: "))
    while user_guess != answer:
        if user_guess < answer:
            user_guess = int(input("Too low! Try again: "))
        elif user_guess > answer:
            user_guess = int(input("Too high! Try again: "))
    print("You guessed it! You won!")
    while keep_playing != "y" or keep_playing != "n":
        keep_playing = input("Do you want to keep playing? (y/n): ")
        keep_playing = keep_playing.lower()
        if keep_playing == "n":
            quit()
        elif keep_playing == "y":
            break