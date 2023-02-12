import time
from selenium import webdriver
from Selenium_funkcje import make_screenshot
from Selenium4 import LoginPage

def test_login_page():
    driver = webdriver.Chrome()
    page = LoginPage(driver, "user-name", "password", "login-button")
    page.open()
    page.enter_username("standard_user")
    page.enter_password("secret_sauces")
    page.click_login_button()
    time.sleep(1)



    driver.quit()