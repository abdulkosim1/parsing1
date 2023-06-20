# # python3 -m venv venv - создание виртуального окружения
# # source venv/bin/activate - активация
# # deactivate - выход
# # pip freeze - список установленных библиотек

# # pip install requests
# # pip install lxml
# # pip install beautifulsoup4


# import requests
# import csv
# from bs4 import BeautifulSoup as BS

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_soup(html):
#     soup = BS(html, 'html.parser')
#     return soup

# def get_data(soup):
#     phones = soup.find_all('div', class_ = 'ty-column4') 

#     for phone in phones:
#         title = phone.find('a', class_ = 'product-title').text.strip()
#         print(title)
#         try:
#             price = phone.find('span', class_="ty-price-num").text
#         except AttributeError:
#             price = None
#         print(price)
#         # break
#         image = phone.find('img', class_='ty-pict').get('data-ssrc')

#         write_csv({
#             'title':title,
#             'image':image,
#             'price':price
#         })
#         print(image)

# def write_csv(data):
#     with open('phones.csv', 'a') as file:
#         names = ['title', 'price', 'image']
#         write = csv.DictWriter(file,delimiter=',',fieldnames=names)
#         write.writerow(data)

# def main():
#     BASE_URL = "https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/"
#     html = get_html(BASE_URL)
#     soup = get_soup(html)
#     get_data(soup)

# task1 ========================
# import requests
# source = requests.get('https://stackoverflow.com/questions').status_code
# print(source)

# task2 ========================
# import requests
# import csv
# from bs4 import BeautifulSoup as BS
# def get_html(url):
#     response = requests.get(url)
#     return response.text
# def get_soup(html):
#     soup = BS(html, 'lxml')
#     return soup
# def get_data(soup):
#     h1 = soup.find('h1').text
#     print('h1:',h1)
#     p = soup.find('p').text
#     print('p:',p)
#     a = soup.find('a').get('href')
#     print('a:',a)
# BASE_URL = 'http://www.example.com/'
# html = get_html(BASE_URL)
# soup = get_soup(html)
# get_data(soup)

# task3 =========================================
# import requests
# import csv
# from bs4 import BeautifulSoup as BS
# def get_html(url):
#     response = requests.get(url)
#     return response.text
# def get_soup(html):
#     soup = BS(html, 'html.parser')
#     return soup
# def get_data(soup):
#     # s = soup.find_all('a', class_ = 'central-featured-lang lang5')
#     p = soup.find('div', lang = 'de').text
#     print(p)
# BASE_URL = 'https://www.wikipedia.org/'
# html = get_html(BASE_URL)
# soup = get_soup(html)
# get_data(soup)

# task4
# import requests
# from bs4 import BeautifulSoup

# def getTitle(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     title = soup.find('h1')
#     if title:
#         return title
#     else:
#         return "Title could not be found"

# print(getTitle('http://www.example.com/'))

# task5
# import requests
# import csv
# from bs4 import BeautifulSoup as BS
# def get_html(url):
#     response = requests.get(url)
#     return response.text
# def get_soup(html):
#     soup = BS(html, 'html.parser')
#     return soup
# def get_data(soup):
#     s = soup.find_all('div', class_ = 'category width33 vertical-separator')
#     # print(s)
#     for i in s:
#         p = i.find('span', class_='category-product-count').text
#         print(p)
# BASE_URL = 'https://enter.kg'
# html = get_html(BASE_URL)
# soup = get_soup(html)
# get_data(soup)

# task6
import requests
import csv
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'html.parser')
    return soup
title_list = []

def get_data(soup):
    phones = soup.find_all('div', class_ = 'd-track typo-track d-track_selectable d-track_with-cover d-track_with-chart') 
    # print(phones)
    for phone in phones:
        a = phone.find('div', class_='d-track__name')
        b = phone.find('span', class_='d-track__artists')
        img = phone.find('img', class_='entity-cover__image deco-pane')
        img_url = img['src']
        title = a.text.strip()
        artist = b.text
        image = 'https:' + img_url

        write_csv({
            'title':title,
            'artist':artist,
            'image':image
        })

def write_csv(data):
    with open('music.csv', 'a') as file:
        names = ['title', 'artist', 'image']
        write = csv.DictWriter(file,delimiter=',',fieldnames=names)
        write.writerow(data)

# import psycopg2
# import csv

# # создайте подключение к базе данных
# conn = psycopg2.connect("dbname=project user=postgres password=1 host=localhost")
# # откройте CSV файл
# with open('/Users/abdulkosim./Desktop/py25/week5/parsing/music.csv', 'r') as f:
#     # создайте объект csv.reader и прочитайте CSV файл
#     reader = csv.reader(f)
#     # создайте объект курсора
#     cursor = conn.cursor()
#     # выполните команду COPY для копирования данных из CSV файла в таблицу
#     cursor.copy_from(f, 'test_table', sep=',', columns=('title', 'artist', 'image'))
#     # сохраните изменения
#     conn.commit()

def main():
    BASE_URL = "https://music.yandex.ru/chart"
    html = get_html(BASE_URL)
    soup = get_soup(html)
    get_data(soup)

main()

# def get_link(title_list, name):
#     for title in title_list:
#         if name.lower() in title['name'].lower():
#             return title["link"]
#     return None

# print(get_link(title_list, 'Shawshank'))