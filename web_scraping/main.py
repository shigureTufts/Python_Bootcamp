import requests
import bs4

url = "http://quotes.toscrape.com/"
# Requesting HTML from server
content = requests.get(url)
# Check text is HTML and check tags
# print(content.text)

# Soup time
soup = bs4.BeautifulSoup(content.text, 'html.parser')
print(soup.body.span)
