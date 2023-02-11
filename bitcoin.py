import requests
from bs4 import BeautifulSoup as bs

URL = 'https://coinmarketcap.com/currencies/bitcoin/'
r = requests.get(URL)

soup = bs(r.content, 'html.parser')

price = soup.find('div', {'class': 'priceValue'})
extract = price.select_one('span')

print(f'Do you know how much bitcoin costs for today? - \n'
      f'Yes, i do. BITCOIN PRICE IS: {extract.text} per (BTC / USD)')
