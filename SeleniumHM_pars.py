from selenium import webdriver
from time import sleep

class Bot :
    global URL, new_URL
    URL = 'https://www2.hm.com/ru_ru/zhenshchiny/novye-postupleniya/odezhda.html'

    def __init__( self ) :
        self.driver = webdriver.Firefox()
        self.navigate()

    def navigate( self ) :
        self.driver.get(URL)

        button = self.driver.find_element_by_xpath('//button[@class="button js-load-more "]')

        while True :
            try :
                button.click()
                sleep(3)
            except :
                break

        print('I`m done!)')

        file = open('url.txt', 'w')

        file.write(self.driver.current_url)
        file.close()

def main() :
    b = Bot()

if __name__ == '__main__' :
    main()

