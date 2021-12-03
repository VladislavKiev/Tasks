"""
ValConv
"""

import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text, 'html.parser')


table = soup.find('table', {'class': 'table-auto'})
tr = table.find('td', {'class': 'responsive-hide'})
tr_txt = tr.text
tr_txt = tr_txt[:6]
doll = 'USD curr' + str(tr_txt)
print(doll)
