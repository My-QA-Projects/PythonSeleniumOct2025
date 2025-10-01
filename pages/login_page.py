from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import get as get_config


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def navigate_to(self, url=None):
        """Navigate to the given URL or fall back to the configured base_url.

        Accepts an optional url for backwards compatibility with existing tests.
        """
        if url is None:
            url = get_config("base_url")
        if not url:
            raise ValueError("No URL provided and no base_url found in configs/config.json")
        self.driver.get(url)

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
