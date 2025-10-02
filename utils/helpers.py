from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def wait_for_element(driver, locator, timeout=10):
    """Explicit wait for an element to be visible."""
    return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
