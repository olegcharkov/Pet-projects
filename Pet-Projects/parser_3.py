import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import colorama

# data_dict = []
url = 'https://rentride.ru/arendovat/moskva/?min_year=2010&max_year=2022&page=1'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
infos = soup.find_all('div', class_='vehicle-card-vertical-body car-info-body')
max_pages = 23
# n = 1

# map = {}
# id = 0

for p in range(max_pages):
    sleep(1)
    cur_url = url + str(p+1)
    print(colorama.Fore.YELLOW + "Скрапинг страницы #: %d" % (p+1) + colorama.Fore.WHITE)

    for n, i in enumerate(infos, start=1):
        name = i.find('h4', class_='title-car').text.strip()
        stars = i.find('div', class_='rating-value').text.strip()
        comments = i.find('div', class_='car-review-count').text.strip()
        price = i.find('div', class_='car-price-info').text.strip()
        print(f'{n}: {name} цена:{price} с оценкой {stars} и количеством отзывов:{comments}')

        # page_nav = soup.find_all('a', href='https://rentride.ru/arendovat/moskva/?min_year=2010&max_year=2022&page=23')
        # if(len(page_nav)==0):
        #     print(colorama.Fore.LIGHTRED_EX + 'Max_page')
        #     break

