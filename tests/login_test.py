from pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url  # Verify redirect


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("invalid", "invalid")
    error = login_page.get_error_message()
    assert "Username and password do not match" in error
