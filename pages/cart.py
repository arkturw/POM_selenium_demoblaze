import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CartPage:

    # Lokatory obiektów:
    PRODUCT_LIST = By.XPATH, '//table/tbody/tr/td[2]'
    PRODUCT_DELETE = '//tr[td[text()="{0}"]]/td/a'
    PRODUCT_ROWS = By.CLASS_NAME, 'success'
    PRODUCT_ROW = '//tr[@class="success"]/td[text()="{0}"]'

    # Metody klasy
    def __init__(self, browser):
        self.browser = browser

    def delete_product_from_cart(self, product_name):
        try:
            product = By.XPATH, self.PRODUCT_DELETE.format(product_name)
            delete_product = self.browser.find_element(*product)
            delete_product.click()
        except (NoSuchElementException, Exception) as e:
            print('Wystąpił wyjątek: ', e)

    # Asercje
    def is_product_in_cart(self, product_name):
        products = self.browser.find_elements(*self.PRODUCT_LIST)
        products = [product.text for product in products]
        assert product_name in products

    def is_only_product_in_cart(self, product_name):
        products = self.browser.find_elements(*self.PRODUCT_LIST)
        products = [product.text for product in products]
        assert products[0] == product_name and len(products) == 1

    def is_cart_empty(self):
        products_list = self.browser.find_elements(*self.PRODUCT_ROWS)
        assert len(products_list) == 0

    def is_product_not_in_cart(self, product_name):
        product = By.XPATH, self.PRODUCT_ROW.format(product_name)
        product_row = self.browser.find_elements(*product)
        assert len(product_row) == 0
