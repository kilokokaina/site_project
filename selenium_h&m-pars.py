from selenium import webdriver
from time import sleep

class Bot :
    def __init__( self ) :
        self.driver = webdriver.Firefox()
        self.navigate()

    def navigate( self ) :
        self.driver.get('https://www2.hm.com/ru_ru/zhenshchiny/novye-postupleniya/odezhda.html')

        button = self.driver.find_element_by_xpath('//button[@class="button js-load-more "]')

        while True :
            try :
                button.click()
                sleep(5)
            except :
                break

        print('I`m done!)')

def main() :
    b = Bot()

if __name__ == '__main__' :
    main()
