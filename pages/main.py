from selenium.webdriver.common.by import By


class MainPage:

    # Adres strony
    URL = 'https://www.demoblaze.com/'

    # Lokatory obiektów
    LOGIN_BUTTON = (By.XPATH, '//div/ul/li/a[@id="login2"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def go_to_login_page(self):
        login_btn = self.browser.find_element(*self.LOGIN_BUTTON)
        login_btn.click()




