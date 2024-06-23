from termcolor import colored

text = colored("Hi There", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)
