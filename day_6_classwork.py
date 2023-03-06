import requests
from bs4 import BeautifulSoup
import lxml

HOST = "https://www.nike.com/"
URL = "https://www.nike.com/w/jordan-1-aj85g"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

def get_html(URL, HEADERS, params=""): 
    response = requests.get(url=URL, headers=HEADERS, params=params)
    return response
    

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='product-card product-grid__card css-c2ovjx')

    nike = []

    for item in items:
        nike.append(
            {
             'title': item.find('div', class_='product-card__body').find('a').get_text(),
            "link": item.find("div", class_="product-card__body").find("a").get("href"),
            "category": item.find("div", class_="product-card__subtitle").get_text(strip=True),
            "price": item.find("div", class_="product-price us__styling is--current-price css-11s12ax").get_text(strip=True),
            "img_link": item.find("div", class_="product-card__body"). find("img").get("src"),
             }
        )
    return nike

html = get_html(URL=URL, HEADERS=HEADERS)
content = get_content(html=html.text)

with open("parseNike.txt", "w") as f:
    f.write(str(content))

def parse(content): 
    items = [] 
    for ind, item in enumerate(content): 
        items.append(f'''Товар №: {ind +1} Название: {item['title']}\nСсылка на товар: {item['link']}\nКатегория: {item['category']}\nЦена: {item['price']}\n------------\n''') 
    return items 
shoes = parse(content)
