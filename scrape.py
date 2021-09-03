import requests
from bs4 import BeautifulSoup
from array import *

amazon_url = 'https://www.amazon.co.uk/s?k=hp+charger&rh=n%3A340831031%2Cp_89%3AHP&dc&crid=CWBP4E9PL7IA&qid=1630655136&rnid=1632651031&sprefix=hp+charger%2Caps%2C320&ref=sr_nr_p_89_1'
aliexpress_url = 'https://www.aliexpress.com/af/hp-charger.html?d=y&origin=n&SearchText=hp+charger&catId=0&initiative_id=SB_20210902223906'
ebay_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=hp+charger&_sacat=0&rt=nc&Brand=HP&_dcat=31510'
# setting user-agent
headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

# For amazon


def amazon_product():
    page = requests.get(url=amazon_url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    # print(soup.prettify())

    # title
    title = soup.find('span', class_ ="a-size-base-plus a-color-base a-text-normal")
    text = title.get_text()
    product_title = text.strip()
    print(product_title)

    # price
    price = soup.find(class_= "a-price-whole")
    price = price.get_text()
    amazon_product_price = price.strip()
    return amazon_product_price
    
# for aliexpress


def aliexpress_product():
    page = requests.get(url=aliexpress_url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    # print(soup.prettify())

    # title
    title = soup.find('span', id_ ="a2g0o.productlist.0.i33.5df73d91X4KbfP")
    text = title.get_text()
    product_title = text.strip()
    print(product_title)

    # price
    price = soup.find(class_= "_12A8D")
    price = price.get_text()
    aliexpress_product_price = price.strip()
    return aliexpress_product_price


     
    
# for ebay


def ebay_product():
    page = requests.get(url=ebay_url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    # print(soup.prettify())

    # title
    title = soup.find('span', class_="BOLD")
    text = title.get_text()
    product_title = text.strip()
    print(product_title)

    # price
    price = soup.find(class_="s-item__price")
    price = price.get_text()
    ebay_product_price = price.strip()
    return ebay_product_price


def getPrices():
    # amazon_product_price = float(amazon_product()[1:])
    # aliexpress_product_price = float(aliexpress_product()[1:])
    # ebay_product_price = float(ebay_product()[1:])
    amazon = amazon_url 
    aliexpress = aliexpress_url
    ebay = ebay_url 
    #URL = array ('u', amazon, aliexpress,ebay) 
    return [ amazon, aliexpress, ebay]

