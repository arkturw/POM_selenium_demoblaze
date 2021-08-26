from selenium.webdriver.common.by import By

from time import sleep


class MainPage:

    # Adres strony
    URL = 'https://www.demoblaze.com/'

    # Lokatory obiektów
    BUTTON_LOGIN = (By.XPATH, '//div/ul/li/a[@id="login2"]')
    BUTTON_LOGIN_CONFIRM = (By.XPATH, '//div/button[text()="Log in"]')
    INPUT_USERNAME = (By.ID, 'loginusername')
    INPUT_PASSWORD = (By.ID, 'loginpassword')
    TEXT_USERNAME = '//div/ul/li/a[@id="nameofuser" and contains(text(), "{0}")]'

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
        # sleep(3)

    def is_username_visible(self, username):
        try:
            username_text = self.browser.find_element(By.XPATH,
                                                      self.TEXT_USERNAME.format(username))
            if username_text.is_displayed():
                return True
            else:
                return False
        except Exception as err:
            print('Wystąpił wyjątek: ', err)
            return False

    def is_wrong_password_message_displayed(self):
        try:
            alert_text = self.browser.switchTo().alert().getText()
            assert 'Wrong password.' in alert_text, 'Brak alertu.'
        except Exception as err:
            print('Wystąpił wyjątek: ', err)
            return False
