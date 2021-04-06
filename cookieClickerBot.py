from selenium import webdriver
from settings import Settings
import time

class CookieClickerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(Settings.PATH)
        self.driver.get(Settings.URL)
        self.driver.implicitly_wait(5)

        self.cookie = self.driver.find_element_by_id('bigCookie')
        self.cookie_counter = self.driver.find_element_by_id('cookies')
        self.clickCookie = lambda times: [self.cookie.click() for i in range(times)]
        self.main()

    def main(self):
        while True:
            self.clickCookie(1000)

            buildings = self.driver.find_elements_by_css_selector('.product.unlocked.enabled')
            [[building.click() for i in range(5)] for building in buildings[::-1]]

            # upgrades = self.driver.find_elements_by_css_selector('.crate.upgrade.enabled')
            # if upgrades:
                # upgrades[-1].click()
            # [upgrade.click() for upgrade in upgrades[::-1]]


if __name__ == '__main__':
    bot = CookieClickerBot()
