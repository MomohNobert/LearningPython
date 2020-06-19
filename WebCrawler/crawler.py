import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.jumia.com.ng/watches-sunglasses/?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features='html.parser')

        for link in soup.findAll('a', {'class': 'core'}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
            # get_single_item_data(href)
            print()
        page += 1

# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, features='html.parser')

#     for item_name in soup.findAll('a', {'class': 'i-name'}):
#         print(item_name.string)
#     for link in soup.findAll('a'):
#         href = 'https://www.jumia.ng' + link.get('href')
#         print(href)


trade_spider(1)

