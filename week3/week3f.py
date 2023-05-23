import requests
from bs4 import BeautifulSoup
import re

"""
ORTALAMA = lambda values: sum(values) / len(values)

prices = []

for i in range(4):
    url = "https://www.bisikletsepeti.com/k/bisiklet/?probrand=&proprice=&procolour=&prosize=&protag=&prosort=&prostock=&propage=" + str(i+1)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    mydivs = soup.find_all("span", {"class": "ProBox-Price"})

    for mydiv in mydivs:
        mydiv = re.sub("[^\d\,]", "", str(mydiv))
        mydiv = mydiv.replace(",", ".")
        mydiv = float(mydiv)
        prices.append( mydiv )


print(len(prices))
print(ORTALAMA( prices ))
"""

"""
url = "https://www.robotsepeti.com/raspberry-pi-kart"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
mydivs = soup.find_all("span", {"itemprop": "price"})

for mydiv in mydivs:
    data = mydiv.attrs['content']
    data = float(str(data))
    print(data, type(data))
"""



url = "https://www.bakuelectronics.az/catalog/telefonlar-qadcetler/smartfonlar-mobil-telefonlar/"
req = requests.get(url)

# 'xml' is the parser used. For html files, which BeautifulSoup is typically used for, it would be 'html.parser'.
soup = BeautifulSoup(req.text, 'lxml')

mydivs = soup.find_all("div", {"class": "product__card"})


products = []

for mydiv in mydivs:
    if mydiv.attrs['class'] == ['product__card']:
        product = {
            "price": float(str(mydiv.attrs['data-product-price']).replace(",", ".")),
            "name": mydiv.attrs['data-product-name'],
            "brand": mydiv.attrs['data-product-brand'],
            "category": mydiv.attrs['data-product-category']

        }
        products.append(product)

print(products)
import json

json.dump( products, open('w3products.json', 'w') )

