
import requests
from bs4 import BeautifulSoup

url_weather = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2'
url_curr = 'https://minfin.com.ua/currency/nbu/'
url_price = 'https://index.minfin.com.ua/markets/fuel/tm/okko/'

source_weather = requests.get(url_weather)
main_text = source_weather.text
soup_weather = BeautifulSoup(main_text, 'html.parser')

tmp = soup_weather.find('p', {'class': 'today-temp'})
tmp_txt = tmp.text
print('Now in Kiev', tmp_txt)

min_t = soup_weather.find('div', {'class': 'min'})
min_t_txt = min_t.text
min_t_txt = min_t_txt[5:]
max_t = soup_weather.find('div', {'class': 'max'})
max_t_txt = max_t.text
max_t_txt = max_t_txt[7:]
print('Min temp today is ', min_t_txt, 'C', 'Max temp today is ', max_t_txt, 'C')


all_day = soup_weather.findAll('div', {'class': 'temperature'})
tomorrow_temp = all_day[2]
t_min_temp = tomorrow_temp.find('div', {'class': 'min'})
t_min_temp = t_min_temp.text[5:]
t_max_temp = tomorrow_temp.find('div', {'class': 'max'})
t_max_temp = t_max_temp.text[7:]
print('Min temp tomorrow is ', t_min_temp, 'C', 'Max temp tomorrow is ', t_max_temp, 'C')

source_curr = requests.get(url_curr)
main_text = source_curr.text
soup_curr = BeautifulSoup(main_text, 'html.parser')


table = soup_curr.find('table', {'class': 'table-auto'})
tr = table.find('td', {'class': 'responsive-hide'})
tr_txt = tr.text
tr_txt = tr_txt[:6]
print('USD curr', tr_txt)

source_price = requests.get(url_price)
main_text = source_price.text
soup_price = BeautifulSoup(main_text, 'html.parser')

price = soup_price.findAll('td', {'align': 'right'})
price_95plus = price[0]
price_95 = price[3]
price_92 = price[6]
price_95plus_txt = price_95plus.text
price_95_txt = price_95.text
price_92_txt = price_92.text


print('OKKO 95+', price_95plus_txt)
print('OKKO 95', price_95_txt)
print('OKKO 92', price_92_txt)
