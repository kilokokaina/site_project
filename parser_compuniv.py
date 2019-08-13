import urllib.request
from bs4 import BeautifulSoup

class AppURLopener(urllib.request.FancyURLopener) :
    version = 'Mozilla/5.0'

URL = 'https://www.computeruniverse.net/ru/c/notebooks-tablets-pcs/notebooks-zubehor'

def get_html( url ) :
    opener = AppURLopener()
    response = opener.open(url)
    return response.read()

def get_page_count( html ) :
    soup = BeautifulSoup(html, 'html.parser')
    page_list = soup.find('div', class_ = 'pager')
    return int(page_list.find_all('li')[-3].text)

def parse( html ) :
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_ = 'item-grid')

    items = []

    for row in table.find_all('div', class_ = 'item-box') :
        cols = row.find_all('a')
        price = row.find_all('div', class_ = 'product-price')
        availab = row.find_all('div', class_ ='availability')

        items.append({
            'title' : cols[1].text,
            'price' : price[0].text,
            'inStock' : availab[0].text
        })

    # for item in items :
    #     print(item)
    return items

def main():
    page_count = get_page_count(get_html(URL))

    print('Всего найдено страниц:', page_count)

    items = []

    for page in range(1, page_count) :
        print('Парсинг: ', (page / page_count * 100), '%')
        items.extend(parse(get_html(URL)))

    for item in items :
        print(item)

if __name__ == '__main__' :
    main()
