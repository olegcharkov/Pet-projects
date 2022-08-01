import requests
from bs4 import BeautifulSoup
import json


url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')


for n, i in enumerate(items, start=1):
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{n}: {itemPrice} за {itemName}')


pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        hrefval = link.get('href')
        urls.append(hrefval)


data_dict = []
for slug in urls:
    newUrl = url.replace('?page=1', slug)
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_= 'col-lg-4 col-md-6 mb-4')
    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemPrice} за {itemName}')

    data = {
        'Item': itemName,
        'Price': itemPrice,
        }

    data_dict.append(data)

    with open('data.json', 'w') as json_file:
        json.dump(data_dict, json_file, indent=5)