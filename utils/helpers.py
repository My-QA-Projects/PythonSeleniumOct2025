from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, locator, timeout=10):
    """Explicit wait for an element to be visible."""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
