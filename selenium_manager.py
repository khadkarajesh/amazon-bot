from selenium import webdriver
from selenium.webdriver.common import keys


class SeleniumManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.driver = webdriver.Chrome("./chromedriver")

    def _initialize(self):
        pass

    def search(self):
        self.driver.get(self.base_url)
        search_bar = self.driver.find_element_by_name("q")
        search_bar.send_keys("getting started with python")
        search_bar.send_keys(keys.Keys.RETURN)
        search_bar.clear()
