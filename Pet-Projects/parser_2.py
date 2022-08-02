import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import colorama

data_dict = []
url = 'https://rentride.ru/arendovat/moskva/'
n = 1
params = {'page': 1}

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
last_page_num = int(soup.find_all('a', class_='pagination-number-item')[-1].text)

for page_num in range(1, last_page_num-1):
    sleep(1)
    params['page'] = page_num
    cur_url = url + str(page_num + 1)
    print(colorama.Fore.YELLOW + "Скрапинг страницы #: %d" % (page_num) + colorama.Fore.WHITE)
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    infos = soup.find_all('div', class_='vehicle-card-vertical-body car-info-body')

    for n, i in enumerate(infos, start=n):
        name = i.find('h4', class_='title-car').text.strip()
        stars = i.find('div', class_='rating-value').text.strip()
        comments = i.find('div', class_='car-review-count').text.strip()
        price = i.find('div', class_='car-price-info').text.strip()
        print(f'{n}: {name} цена:{price} с оценкой {stars} и количеством отзывов:{comments}')

        data = {
            'car': name,
            'price': price,
            'stars': stars,
            'comments': comments,
        }

        data_dict.append(data)

with open('data_2.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=5)
