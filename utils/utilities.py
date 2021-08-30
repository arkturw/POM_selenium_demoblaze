from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_alert(driver: object, seconds: int = 5):
    try:
        wait = WebDriverWait(driver, seconds)
        wait.until(EC.alert_is_present())
        return True
    except (NoSuchElementException,
            TimeoutException,
            Exception) as e:
        print('Wystąpił wyjątek: ', e)
        return False
