import pytest
from selenium.webdriver import Firefox

from pages.index import IndexPage
from test_data.data import UserData


# Przygotowanie drivera
@pytest.fixture
def browser():
    driver = Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_add_laptop_to_cart(browser):
    # Załadowanie danych testowych
    user_data = UserData()
    # Strona główna
    main_page = IndexPage(browser)
    main_page.load()
    main_page.open_login_popup()
    # Logowanie
    main_page.log_in(user_data.get_name(),
                     user_data.get_password()
                     )
    # Dodanie laptopa do koszyka
    main_page.wait_for_login_modal_to_disappear()
    main_page.go_to_category('Laptops')
