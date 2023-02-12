import time
from selenium import webdriver
from Selenium_funkcje import make_screenshot
from Selenium4 import LoginPage
import pytest

test_data = [("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
             ("locked_out_user", "secret_sauce", "https://www.saucedemo.com/"),
             ("problem_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
             ("performance_glitch_user", "secret_sauce", "https://www.saucedemo.com/inventory.html")]


@pytest.mark.parametrize("user, password, url", test_data)
def test_login_page(user, password, url):
    driver = webdriver.Chrome()
    nazwa = driver.title
    page = LoginPage(driver, "user-name", "password", "login-button")
    page.open()
    page.enter_username(user)
    page.password(password)
    page.click_login_button()
    time.sleep(1)
    try:
        assert driver.current_url == url, make_screenshot(driver, nazwa)
    finally:
        driver.quit()
