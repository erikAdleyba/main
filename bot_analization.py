import requests
from bs4 import BeautifulSoup
import pandas as pd

FILE_NAME = "test.csv"


# Отправка GET-запроса к веб-странице
url = 'https://brandshop.ru/muzhskoe/'  # Замените на нужный вам URL-адрес
response = requests.get(url)


req = requests.get(url)
src = req.text



with open("index.html", 'w', encoding="utf-8") as file:
    file.write(src)
   

with open("index.html", encoding="utf-8") as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml' )

all_product = soup.find_all(class_="product-catalog")
#product = all_product[1].text

# for item in all_product :
#      product = item.text

#      print(product)
price_prodect_card = soup.find_all(class_="product-card")    
price_product = soup.find_all(class_="product-card__price")

for i in all_product:

    catalog = i.text
    for y in price_product:
        
        price_all = y.text
    
print(f'{catalog}')
