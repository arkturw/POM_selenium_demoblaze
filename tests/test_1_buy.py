import pytest

from pages.index import IndexPage
from pages.prod import ProductPage
from pages.cart import CartPage
from test_data.data import ProductData, UserData

from fixtures.fixture_setup import browser
from fixtures.fixture_login import log_in


# @pytest.mark.usefixtures('log_in')
def test_add_laptop_to_cart(browser, log_in):
    # Załadowanie danych tesowych produktu
    product = ProductData()
    # Wyszukiwanie produktu
    index_page = log_in
    index_page.go_to_category(product.get_category())
    index_page.find_product_by_name(product.get_name())
    # Przejście na stronę produktu
    product_page = ProductPage(browser)
    product_page.is_expected_product_displayed(product.get_name())
    product_page.add_product_to_cart()
    product_page.is_confirmation_visible()
    product_page.go_to_cart()


# @pytest.fixture(name='check cart')
def test_check_cart(browser, log_in):
    # Załadowanie danych produktu
    product = ProductData()
    # Przejście do koszyka
    index_page = log_in
    index_page.go_to_cart()
    # Przeszukanie koszyka
    cart_page = CartPage(browser)
    cart_page.is_product_in_cart(product.get_name())
    cart_page.is_only_product_in_cart(product.get_name())
