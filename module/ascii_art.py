import pyfiglet
from termcolor import colored
color_list = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")


message = pyfiglet.figlet_format(input("What message do you want to print? "))
color = input("What color? ").lower()

if color in color_list:
    print(colored(message, color=color))
else:
    print(colored(message, color="magenta"))

