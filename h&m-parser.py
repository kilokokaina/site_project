import requests
import urllib.request
from bs4 import BeautifulSoup

URL = 'https://www2.hm.com/ru_ru/zhenshchiny/vybrat-kategoriyu/view-all.html'

class AppURLopener(urllib.request.FancyURLopener) :
    version = 'Mozilla/5.0'

def get_html( url ) :
    opener = AppURLopener()
    response = opener.open(url)
    return response.read()

def main() :
    print(get_html(URL))

if __name__ == '__main__' :
    main()
