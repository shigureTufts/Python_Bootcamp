import pyfiglet
import requests
import termcolor
url = "https://icanhazdadjoke.com/search"

# print out ASCII art
print(termcolor.colored(pyfiglet.figlet_format("Dad Joke 3000"), color="magenta"))
topic = input("Let me tell you a joke! Give me a topic: ")

# connect to server and get response
response = requests.get(url, headers={"Accept": "application/json"}, params={"term": topic, "limit": 1})
data = response.json()

# get joke with related to user input topic
print(f"I'v got {data['total_jokes']} jokes related to {topic}, here is one:")
print(data['results'][0]['joke'])
