from selenium.webdriver import Chrome
from utils.helpers import wait_for_element


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """Find element with wait for reliability."""
        return wait_for_element(self.driver, locator)

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
