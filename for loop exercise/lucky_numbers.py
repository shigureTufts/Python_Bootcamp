number = range(1, 21)
for integer in number:
    if integer % 2 == 0:
        if integer == 4:
            print(f"{number} is Unlucky!!")
        else:
            print(f"{number} is even!!")
    else:
        if integer == 13:
            print(f"{number} is Unlucky!!")
        else:
            print(f"{number} is odd!!")