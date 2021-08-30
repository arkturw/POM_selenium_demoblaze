from selenium.webdriver import Firefox
import pytest


# Przygotowanie drivera
@pytest.fixture
def browser():
    driver = Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
