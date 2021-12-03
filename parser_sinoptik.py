
import requests
from bs4 import BeautifulSoup

url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text, 'html.parser')

tmp = soup.find('p', {'class': 'today-temp'})
tmp_txt = tmp.text
print('Now in Kiev', tmp_txt)
min_t = soup.find('div', {'class': 'min'})
min_t_txt = min_t.text
min_t_txt = min_t_txt[5:]
print('Min temp today is ', min_t_txt, 'C')
max_t = soup.find('div', {'class': 'max'})
max_t_txt = max_t.text
max_t_txt = max_t_txt[7:]
print('Max temp today is ', max_t_txt, 'C')


all_day = soup.findAll('div', {'class': 'temperature'})
tomorrow_temp = all_day[2]
t_min_temp = tomorrow_temp.find('div', {'class': 'min'})
t_min_temp = t_min_temp.text[5:]
print('Min temp tomorrow is ', t_min_temp, 'C')
t_max_temp = tomorrow_temp.find('div', {'class': 'max'})
t_max_temp = t_max_temp.text[7:]
print('Max temp tomorrow is ', t_max_temp, 'C')
