import pytest

from selenium.webdriver import Firefox


# Przygotowanie drivera
@pytest.fixture(scope='session')
def browser_instance():
    browser_instance = Firefox()
    browser_instance.implicitly_wait(10)
    yield browser_instance
    browser_instance.quit()


@pytest.fixture
def browser(browser_instance):
    yield browser_instance
    browser_instance.delete_all_cookies()
    browser_instance.get('about:blank')
