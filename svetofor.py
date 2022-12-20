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
# import csv
# from bs4 import BeautifulSoup as BS

# def get_html(url):
#     response = requests.get(url)
#     return response.text
# def get_soup(html):
#     soup = BS(html, 'html.parser')
#     return soup

# def getTitle(url):
#     html = get_html(url)
#     soup = get_soup(html)
#     try:
#         a = soup.find('h1')
#         print(a)
#     except AttributeError:
#         print('Title could not be found')

# print(getTitle('http://www.example.com/'))


# task5
