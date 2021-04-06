from selenium import webdriver
# import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"
URL = r"https://orteil.dashnet.org/cookieclicker/"

class CookieClickerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(URL)
        self.driver.implicitly_wait(5)
        self.clickCookie = lambda times: [self.driver.find_element_by_id('bigCookie').click() for i in range(times)]
        self.main()

    def clickFirstUpgrade(self):
        try:
            self.driver.find_element_by_id('upgrade0').click()
        except:
            print('clickFirstUpgrade exception')

    def clickBuildings(self):
        buildings = self.driver.find_elements_by_css_selector('.product.unlocked.enabled')
        [[building.click() for i in range(5)] for building in buildings[::-1]]

    def main(self):
        while True:
            self.clickCookie(200)
            self.clickFirstUpgrade()
            self.clickBuildings()


if __name__ == '__main__':
    bot = CookieClickerBot()
