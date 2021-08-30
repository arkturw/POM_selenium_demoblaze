from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CartPage:

    # Lokatory obiektów:
    PRODUCT_LIST = By.XPATH, '//table/tbody/tr/td[2]'

    # Metody klasy
    def __init__(self, browser):
        self.browser = browser

    # Asercje
    def is_product_in_cart(self, product_name):
        products = self.browser.find_elements(*self.PRODUCT_LIST)
        products = [product.text for product in products]
        assert product_name in products

    def is_only_product_in_cart(self, product_name):
        products = self.browser.find_elements(*self.PRODUCT_LIST)
        products = [product.text for product in products]
        assert products[0] == product_name and len(products) == 1
