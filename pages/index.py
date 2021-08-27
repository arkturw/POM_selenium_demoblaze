import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from utils.utilities import wait_for_alert
from time import sleep


class IndexPage:

    # Adres strony
    URL = 'https://www.demoblaze.com/'

    # Lokatory obiektów
    BUTTON_LOGIN = By.XPATH, '//div/ul/li/a[@id="login2"]'
    BUTTON_LOGIN_CONFIRM = By.XPATH, '//div/button[text()="Log in"]'
    INPUT_USERNAME = By.ID, 'loginusername'
    INPUT_PASSWORD = By.ID, 'loginpassword'
    MODAL_LOGIN = By.ID, 'logInModal'
    TEXT_USERNAME = '//div/ul/li/a[@id="nameofuser" and contains(text(), "{0}")]'
    LINK_CATEGORY = '//a[@id="itemc" and text()="{0}"]'

    # Metody klasy
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def open_login_popup(self):
        login_btn = self.browser.find_element(*self.BUTTON_LOGIN)
        login_btn.click()

    def log_in(self, username, password):
        username_input = self.browser.find_element(*self.INPUT_USERNAME)
        password_input = self.browser.find_element(*self.INPUT_PASSWORD)
        login_confirm = self.browser.find_element(*self.BUTTON_LOGIN_CONFIRM)
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_confirm.click()

    def wait_for_login_modal_to_disappear(self):
        # Czekam na zniknięcie modalu logowania, jesli jest widoczny
        if EC.visibility_of_element_located(self.MODAL_LOGIN):
            WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(self.MODAL_LOGIN))

    def go_to_category(self, category):
        link = (By.XPATH, self.LINK_CATEGORY.format(category))
        category_link = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(link))
        category_link.click()

    def find_product_by_name(self, product_name):
        try:
            product = self.browser.find_element(By.LINK_TEXT, product_name)
            product.click()
        except NoSuchElementException as e:
            print('Wystąpił wyjątek: ', e)
            return False

    # Asercje
    def is_username_visible(self, username):
        username_text = self.browser.find_element(By.XPATH,
                                                  self.TEXT_USERNAME.format(username)
                                                  )
        assert username_text.is_displayed()

    def is_wrong_password_message_displayed(self):
        wait_for_alert(self.browser)
        alert = self.browser.switch_to.alert
        assert 'Wrong password.' in alert.text
        alert.accept()
