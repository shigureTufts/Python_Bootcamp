import requests
from bs4 import BeautifulSoup
from time import sleep
import json

base_url = "http://quotes.toscrape.com"
url = "/page/1/"
all_quotes = []
# Check text is HTML and check tags
while url:
    # Requesting HTML from server
    content = requests.get(f"{base_url}{url}")
    print(f"scraping {base_url}{url}")

    # get quotes from page 1
    soup = BeautifulSoup(content.text, 'html.parser')
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_='text').get_text(),
            "author": quote.find(class_='author').get_text(),
            "bio-link": quote.find("a")["href"]
        })

    # navigate to the next page
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    sleep(3)

# testing quotes
for quote in all_quotes:
    print(quote)

# write all the quote into the file
with open("quotes.txt", "w") as file:
    file.write(json.dumps(all_quotes))
