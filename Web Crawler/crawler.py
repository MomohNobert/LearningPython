import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.jumia.com.ng/watches-sunglasses/?page=2'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)

        for link in soup.findAll('a', {'class': 'core'}):
            href = link.get('href')
            print(href)
        page += 1

trade_spider(1)

