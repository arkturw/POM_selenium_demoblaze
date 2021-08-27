from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_alert(driver:object, seconds:int=5):
    try:
        wait = WebDriverWait(driver, seconds)
        wait.until(EC.alert_is_present())
        return True
    except exceptions.NoSuchElementException as e:
        print('Wystąpił wyjątek: ', e)
        return False
    except exceptions.TimeoutException as e:
        print('Wystąpił wyjątek: ', e)
        return False
    except Exception as e:
        print('Wystąpił wyjątek: ', e)
        return False