import pytest
from utils.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    """Create a browser instance using the central driver factory.

    This fixture delegates to `utils.driver_factory.get_driver()` which reads
    the `configs/config.json` settings. Override the browser in tests by
    passing a `browser_override` or adding a pytest CLI option (optional).
    """
    driver = get_driver()
    yield driver
    driver.quit()
