import os
import time

from selenium import webdriver


class SeleniumManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.driver = webdriver.Chrome("./chromedriver")
        self.success = False

    def login(self):
        self.driver.get(self.base_url)
        account_element = self.driver.find_element_by_id("nav-link-accountList")
        account_element.click()

        time.sleep(1)

        email_element = self.driver.find_element_by_id("ap_email")

        for char in os.environ.get('USERNAME'):
            time.sleep(1)
            email_element.send_keys(char)

        continue_btn = self.driver.find_element_by_id("continue")
        continue_btn.submit()

        password_element = self.driver.find_element_by_id("ap_password")
        for char in os.environ.get('PASSWORD'):
            time.sleep(1)
            password_element.send_keys(char)

        sign_in_btn = self.driver.find_element_by_id("signInSubmit")

        sign_in_btn.submit()

        time.sleep(1)

    def search(self, item_title):
        # self.driver.get(self.base_url)

        search_bar = self.driver.find_element_by_id("twotabsearchtextbox")

        for key in item_title:
            time.sleep(1)
            search_bar.send_keys(key)

        search_bar.submit()
        time.sleep(3)

        elements = self.driver.find_elements_by_css_selector(".a-link-normal.a-text-normal")
        if len(elements) > 0:
            elements[0].click()
            time.sleep(4)
            cart_btn = self.driver.find_element_by_id("add-to-cart-button")
            cart_btn.submit()
            self.success = True
        return self.success
