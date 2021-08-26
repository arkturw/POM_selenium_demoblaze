from selenium.webdriver.common.by import By
from time import sleep


class ProductPage:

    HEADER_PRODUCT_NAME = By.CLASS_NAME, 'name'
    BUTTON_ADD_TO_CART = By.XPATH, '//div/a[text()="Add to cart"]'

    def __init__(self, browser):
        self.browser = browser

    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*self.BUTTON_ADD_TO_CART)
        add_to_cart_button.click()

    # Asercje
    def is_expected_product_displayed(self, expected_name):
        try:
            product_name = self.browser.find_element(*self.HEADER_PRODUCT_NAME)
            assertion_message = f'Oczekiwana nazwa produktu ({0}) nie jest widoczna', expected_name
            assert product_name.is_displayed(), assertion_message
            return True
        except Exception as err:
            print('Wystąpił wyjątek: ', err)
            return False

    def is_confirmation_visible(self):
        try:
            alert = self.browser.switch_to.alert
            assert 'Product added.' in alert.text, 'Brak alertu.'
            alert.accept()
        except Exception as err:
            print('Wystąpił wyjątek: ', err)
            return False
