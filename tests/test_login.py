import pytest
from selenium.webdriver import Firefox

from pages.index import IndexPage
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
    # Załadowanie danych testowych
    user_data = UserData()
    # Strona główna
    index_page = IndexPage(browser)
    index_page.load()
    index_page.open_login_popup()
    # Logowanie
    index_page.log_in(user_data.get_name(),
                     user_data.get_password()
                     )
    # Asercja
    index_page.is_username_visible(user_data.get_name())


def test_login_negative_password(browser):
    # Załądowanie danych testowych
    user_data = UserData()
    # Strona główna
    main_page = IndexPage(browser)
    main_page.load()
    main_page.open_login_popup()
    # Logowanie
    main_page.log_in(user_data.get_name(),
                     user_data.get_wrong_password()
                     )
    # Asercja
    main_page.is_wrong_password_message_displayed()
