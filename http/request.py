import requests
url = "https://www.google.com"


response = requests.get(url)
print(f"Your request to {url} came back with status code: {response.status_code}")
