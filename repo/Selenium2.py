from selenium import webdriver
# from selenium.webdriver.common.by import By
import time
import datetime

teraz = datetime.datetime.now()


driver = webdriver.Chrome()
driver.get("http://www.saucedemo.com")
print("Nazwa strony:", driver.title)
screenshot = driver.title + teraz.strftime(" %d-%b-%y-%H%M%S") + ".png"
try:
    pole_user = driver.find_element("id", "user-name")
    pole_user.clear()
    pole_user.send_keys("standard_user")
except:
    driver.get_screenshot_as_file(screenshot)
pole_haslo = driver.find_element("id", "password")
pole_haslo.clear()
pole_haslo.send_keys("secret_sauce")
pole_login = driver.find_element("id", "login-button")
pole_login.click()
time.sleep(1)
driver.get_screenshot_as_file(screenshot)
driver.quit()


