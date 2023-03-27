import requests
from bs4 import BeautifulSoup

url = ""
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
shops_div = soup.find("div", {"class": "shops"})

with open("shops.txt", "w") as f:
    f.write(shops_div.h2.text + "\n\n")
    for text in shops_div.stripped_strings:
        f.write(text + "\n")
