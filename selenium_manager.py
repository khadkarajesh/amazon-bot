import os
import time

from selenium import webdriver

ACCOUNT_ID = "nav-link-accountList"
EMAIL_ID = "ap_email"
CONTINUE_ID = "continue"
APP_PASSWORD_ID = "ap_password"
SIGN_IN_SUBMIT_ID = "signInSubmit"
SEARCH_BTN_ID = "twotabsearchtextbox"
SEARCH_RESULT_CSS_SELECTOR = ".a-link-normal.a-text-normal"
ADD_TO_CART_BTN_ID = "add-to-cart-button"


class SeleniumManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.driver = webdriver.Chrome("./chromedriver")
        self.success = False

    def __login(self):
        self.driver.get(self.base_url)
        account_element = self.driver.find_element_by_id(ACCOUNT_ID)
        account_element.click()

        time.sleep(1)

        email_element = self.driver.find_element_by_id(EMAIL_ID)

        for char in os.environ.get('USERNAME'):
            time.sleep(1)
            email_element.send_keys(char)

        continue_btn = self.driver.find_element_by_id(CONTINUE_ID)
        continue_btn.submit()

        password_element = self.driver.find_element_by_id(APP_PASSWORD_ID)
        for char in os.environ.get('PASSWORD'):
            time.sleep(1)
            password_element.send_keys(char)

        sign_in_btn = self.driver.find_element_by_id(SIGN_IN_SUBMIT_ID)

        sign_in_btn.submit()

        time.sleep(1)

    def search(self, item_title):
        self.__login()

        search_bar = self.driver.find_element_by_id(SEARCH_BTN_ID)

        for key in item_title:
            time.sleep(1)
            search_bar.send_keys(key)

        search_bar.submit()
        time.sleep(3)

        elements = self.driver.find_elements_by_css_selector(SEARCH_RESULT_CSS_SELECTOR)
        if len(elements) > 0:
            elements[0].click()
            time.sleep(4)
            cart_btn = self.driver.find_element_by_id(ADD_TO_CART_BTN_ID)
            cart_btn.submit()
            self.success = True
        return self.success
