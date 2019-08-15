import urllib.request
from bs4 import BeautifulSoup

URL = input('Введите аддрес каталога на сайте radiolav.ru: ')

def get_html( url ) :
    response = urllib.request.urlopen(url)
    return response.read()

def get_page_count( html ) :
    soup = BeautifulSoup(html, 'html.parser')
    page_list = soup.find('div', class_ = 'bx-pagination-container row')
    
    if page_list == None :
        return 1
    else :
        return int(page_list.find_all('li')[-2].text)

def parse( html ) :
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id = 'catalogTableList')

    items = []

    for row in table.find_all('div', class_ = 'itemRow item') :
        cols = row.find_all('a')
        # print(cols)

        items.append({
            'title' : cols[1].text,
            'price' : cols[2].text[0 : 15].strip(),
            'inStock' : cols[4].text
        })

    return items

def main() :
    page_count = get_page_count(get_html(URL))

    print('Всего найдено страниц:', page_count)

    items = []

    if page_count == 1 :
        items.extend(parse(get_html(URL))
        
        for item in items :
            print(item)
    else :
        for page in range(1, page_count) :
            print('Парсинг: ', (page / page_count * 100), '%')
            items.extend(parse(get_html(URL + '?PAGEN_1=%d' % page)))

        for item in items :
            print(item)

if __name__ == '__main__' :
    main()
