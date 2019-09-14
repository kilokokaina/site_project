import urllib.request
from bs4 import BeautifulSoup
from SeleniumHM_pars import *

class AppURLopener(urllib.request.FancyURLopener) :
    version = 'Mozilla/5.0'

def get_html( url ) :
    opener = AppURLopener()
    response = opener.open(url)
    return response.read()

def parser( html ) :
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('ul', class_ = "products-listing small")

    items = []

    for row in table.find_all('li', class_ = "product-item") :
        cols = row.find_all('a', class_ = 'link')
        price = row.find_all('span', class_ = "price regular")

        items.append({
            'title': cols[0].text
        })
        # print(cols)

    print(items)

def main() :
    b = Bot()
    print(parser(get_html(URL)))

if __name__ == '__main__' :
    main()

