import time
from selenium import webdriver
from Selenium_funkcje import make_screenshot
from Selenium4 import LoginPage
import pytest


@pytest.mark.parametrize("uzytkownik", ["standard_user", "standard_user2"])

def test_login_page(uzytkownik):
    driver = webdriver.Chrome()
    nazwa = driver.title
    page = LoginPage(driver, "user-name", "password", "login-button")
    page.open()
    page.enter_username(uzytkownik)
    page.password("secret_sauce")
    page.click_login_button()
    time.sleep(1)
    try:
        assert driver.current_url == "https://www.saucedemo.com/inventory.html", make_screenshot(driver, nazwa)
    finally:
        driver.quit()