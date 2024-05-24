number = range(1, 21)
for integer in number:
    if integer % 2 == 0:
        if integer == 4:
            print(f"{integer} is Unlucky!!")
        else:
            print(f"{integer} is even!!")
    else:
        if integer == 13:
            print(f"{integer} is Unlucky!!")
        else:
            print(f"{integer} is odd!!")