from selenium import webdriver
import time
import datetime


def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = driver.title + teraz.strftime(" %d-%b-%y-%H%M%S") + ".png"
    driver.get_screenshot_as_file(screenshot)


driver = webdriver.Chrome()
driver.get("http://www.saucedemo.com")
print("Nazwa strony:", driver.title)

try:
    pole_user = driver.find_element("id", "user-name")
    pole_user.clear()
    pole_user.send_keys("standard_user")
except:
    make_screenshot(driver)

pole_haslo = driver.find_element('xpath','//*[@id="password"]')
pole_haslo.clear()
pole_haslo.send_keys("secret_sauce")
pole_login = driver.find_element("id", "login-button")
pole_login.click()
time.sleep(1)
make_screenshot(driver)
driver.quit()


