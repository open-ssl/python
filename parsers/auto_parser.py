# -- coding: utf-8 --
import requests
import sys
from bs4 import BeautifulSoup
import csv
import unittest
import os

# 3.7.1.
HOST = 'https://auto.ria.com'
URL = f'{HOST}/newauto/marka-lexus/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': '*/*'
}
FILE = 'cars.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.encode('utf8'))
    items = soup.find_all('div', class_='proposition')
    cars = []
    for item in items:
        item1 = item.find('h3', class_='proposition_name')
        item2 = item.find('div', class_='proposition_equip size13 mt-5')
        link = item1.find('a').get('href')
        price_in_dollars = item.find('span', class_='green bold size18').get_text(strip=True)
        price_in_gr = item.find('span', 'grey size13').get_text()
        item1 = item1.find('strong').get_text(strip=True)
        item2 = item2.find('a').get_text()
        cars.append({
            'title': f'{item1} {item2}',
            'link': f'{HOST}{link}',
            'price_in_dollars': price_in_dollars,
            'price_in_gr': price_in_gr
        })
    # for i in cars:
    #     print(i)
    return cars

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', 'mhide')
    count = len(pagination) -1
    return count if count != -1 else 1

    # for rec in pagination:
        # print(rec.encode('utf-8'))

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        # print(html.text.encode('utf8'))
        cars = []
        count = get_pages_count(html.text)
        for page in range(1, count + 1):
            print(f'Парсинг страницы {page} из {count}'.encode('Windows-1251'))
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        print(f'Получено: {len(cars)} автомобилей')
        save_file(cars, FILE)
        os.startfile(FILE)
        # cars = get_content(html.text)
    else:
        print('все плохо')

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Цена в долларах', 'Цена в гривнах'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price_in_dollars'], item['price_in_gr']])




# print(sys.version)
# print('all ok')
# print(get_html(URL).headers)
# print(get_html(URL).__dict__.keys())
parse()
