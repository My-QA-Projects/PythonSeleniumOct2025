from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.config import get as get_config


def _chrome_driver(headless: bool):
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    # Common CI flags
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=service, options=options)


def _firefox_driver(headless: bool):
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("--headless")
    return webdriver.Firefox(service=service, options=options)


def get_driver(browser_override: str = None):
    """Create a WebDriver using settings from configs/config.json.

    browser_override lets callers temporarily override the configured browser
    (useful for pytest CLI overrides).
    """
    browser = (browser_override or get_config("browser", "chrome")).lower()
    headless = get_config("headless", False)
    implicit = get_config("implicit_wait", 5)

    if browser == "chrome":
        driver = _chrome_driver(headless)
    elif browser in ("firefox", "ff", "gecko"):
        driver = _firefox_driver(headless)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(implicit)
    try:
        driver.maximize_window()
    except Exception:
        # Some headless environments don't support window resizing — ignore.
        pass
    return driver
