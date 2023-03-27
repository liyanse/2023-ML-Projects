import requests
from bs4 import BeautifulSoup

url = ''

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

events = soup.select('li.item.event-item.box-link')

with open('events.txt', 'w', encoding='utf-8') as f:
    for event in events:
        date = event.select_one('div.meta-left > span.up-month').text.strip() + ' ' + event.select_one('div.meta-left > span.up-day').text.strip()
        title = event.select_one('div.meta-right > div.title > a > h3').text.strip()
        location = event.select_one('div.meta-right > span.up-venue').text.strip()
        price = event.select_one('div.meta-right > span.tick-price').text.strip()

        print(f'{date} - {title} - {location} - {price}', file=f)
