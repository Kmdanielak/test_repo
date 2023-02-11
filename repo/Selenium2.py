from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.saucedemo.com")
print("Nazwa strony:", driver.title)
pole_user = driver.find_element("id", "user-name")
pole_user.clear()
pole_user.send_keys("standard_user")
pole_haslo = driver.find_element("id", "password")
pole_haslo.clear()
pole_haslo.send_keys("secret_sauce")
pole_login = driver.find_element("id", "login-button")
pole_login.click()

time.sleep(10)
driver.quit()

# button1_accept = driver.find_element("id", "L2AGLb")
# button1_accept.click()
# # print(button1_accept)
# pole_szukaj = driver.find_element("name", "q")
# pole_szukaj.send_keys("python")
# przycisk_szukaj = driver.find_element("name", "btnK")
# przycisk_szukaj.submit()
