import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
# Requesting HTML from server
content = requests.get(url)
# Check text is HTML and check tags
# print(content.text)

# get quotes from page 1
all_quote = []
soup = BeautifulSoup(content.text, 'html.parser')
quotes = soup.find_all(class_="quote")
for quote in quotes:
    all_quote.append({
        "text": quote.find(class_='text').get_text(),
        "author": quote.find(class_='author').get_text(),
        "bio-link": quote.find("a")["href"]
    })

print(all_quote)
