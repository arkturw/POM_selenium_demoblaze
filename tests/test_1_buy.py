import pytest
from selenium.webdriver import Firefox

from pages.index import IndexPage
from pages.prod import ProductPage
from test_data.data import Product, UserData


# Przygotowanie drivera
@pytest.fixture
def browser():
    driver = Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture()
def log_in(browser):
    # Załadowanie danych testowych
    user_data = UserData()
    product = Product()
    # Strona główna
    index_page = IndexPage(browser)
    index_page.load()
    index_page.open_login_popup()
    # Logowanie
    index_page.log_in(user_data.get_name(),
                      user_data.get_password())
    # Dodanie laptopa do koszyka
    index_page.wait_for_login_modal_to_disappear()
    return product


# @pytest.mark.usefixtures('log_in')
def test_add_laptop_to_cart(browser, log_in):
    product = log_in
    index_page = IndexPage(browser)
    index_page.go_to_category(product.get_category())
    index_page.find_product_by_name(product.get_name())
    # Przejście na stronę produktu
    product_page = ProductPage(browser)
    product_page.is_expected_product_displayed(product.get_name())
    product_page.add_product_to_cart()
    product_page.is_confirmation_visible()
    product_page.go_to_cart()
