import pytest
from selenium.webdriver import Firefox

from pages.main import MainPage
from test_data.data import UserData



# Przygotowanie drivera
@pytest.fixture
def browser():
    driver = Firefox()
    driver.implicitly_wait(10)
    # driver.maximize_window()
    yield driver
    driver.quit()


def test_login_positive(browser):
    # Strona główna
    main_page = MainPage(browser)
    main_page.load()
    main_page.go_to_login_page()


def test_login_negative(browser):
    # Strona główna
    main_page = MainPage(browser)
    main_page.load()
    main_page.go_to_login_page()

