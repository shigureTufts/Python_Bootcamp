import pyfiglet
from termcolor import colored

message = pyfiglet.figlet_format(input("What message do you want to print? "))
color = input("What color? ")

print(colored(message, color=color))
