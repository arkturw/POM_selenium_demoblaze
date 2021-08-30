import pytest

from pages.index import IndexPage
from test_data.data import UserData

from fixtures.fixture_setup import (
    browser,
    browser_instance
)


# Zalogowanie użytkownika przed kolejnymi testami
@pytest.fixture
def log_in(browser):
    # Załadowanie danych testowych użytkownika
    user_data = UserData()
    # Strona główna
    index_page = IndexPage(browser)
    index_page.load()
    index_page.open_login_popup()
    # Logowanie
    index_page.log_in(user_data.get_name(),
                      user_data.get_password())
    # Dodanie laptopa do koszyka
    index_page.wait_for_login_modal_to_disappear()
    return index_page
