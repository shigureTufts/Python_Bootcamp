import json
from random import randint
import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"

# load quotes from file
with open("quotes.txt", "r") as file:
    content = json.load(file)

keep_playing = True

if keep_playing:
    # randomly choose one quote
    index = randint(0, len(content))
    quote = content[index]

    # get detail about the quote
    text = quote["text"]
    author = quote["author"]
    bio_link = quote["bio-link"]

    # get author bio
    content = requests.get(f"{base_url}{bio_link}")
    soup = BeautifulSoup(content.text, 'html.parser')
    born_date = soup.find(class_="author-born-date").get_text()
    born_location = soup.find(class_="author-born-location").get_text()
    describe = soup.find(class_="author-description").get_text()
    print(author)

    # start game sequence
    remain_guess = 4
    print("Here is a quote:")
    print(quote["text"])
    guess = input(f"Who said is this? Guesses remaining: {remain_guess}    ")
    if guess.lower() != author.lower():
        print(f"Here is a hint: The author was born in {born_date} {born_location}")
        remain_guess -= 1
        guess = input(f"Who said is this? Guesses remaining: {remain_guess}    ")
    else:
        print('You got it right!')
    if guess.lower() != author.lower():
        print(f"Here is another hint: The author's first name is {author.split()[-1]}")
        remain_guess -= 1
        guess = input(f"Who said is this? Guesses remaining: {remain_guess}    ")
    else:
        print('You got it right!')
    if guess.lower() != author.lower():
        print(f"Here is another hint: The author's last name start with {author.split()[0][0]}")
        remain_guess -= 1
        guess = input(f"Who said is this? Guesses remaining: {remain_guess}    ")
    else:
        print('You got it right!')
    if guess.lower() != author.lower():
        print(f"You ran out if guesses. The answer was {author}")

    user_input = input("Do you want to keep playing?(y/n)   ")
    if user_input.lower == "n":
        keep_playing = False

