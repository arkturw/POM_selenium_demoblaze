from selenium.webdriver.common.by import By
from time import sleep


class ProductPage:

    HEADER_PRODUCT_NAME = By.CLASS_NAME, 'name'
    BUTTON_ADD_TO_CART = By.XPATH, '//div/a[text()="Add to cart"]'
    LINK_CART = By.ID, 'cartur'

    def __init__(self, browser):
        self.browser = browser

    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*self.BUTTON_ADD_TO_CART)
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_link = self.browser.find_element(*self.LINK_CART)
        cart_link.click()

    # Asercje
    def is_expected_product_displayed(self, expected_name):
        try:
            product_name = self.browser.find_element(*self.HEADER_PRODUCT_NAME)
            assertion_message = f'Oczekiwana nazwa produktu ({0}) nie jest widoczna', expected_name
            assert product_name.is_displayed(), assertion_message
            return True
        except Exception as err:
            print('Wystąpił wyjątek 1: ', err)
            return False

    def is_confirmation_visible(self):
        try:
            alert = self.browser.switch_to.alert
            assert 'Product added.' in alert.text, 'Brak alertu.'
            sleep(3)
            alert.accept()
        except Exception as e:
            print('Wystąpił wyjątek 2: ', e)
            return False
