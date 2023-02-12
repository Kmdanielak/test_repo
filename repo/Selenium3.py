from selenium import webdriver
import time
from selenium.webdriver.support import  expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from Selenium_funkcje import  make_screenshot

def czekaj_na_id(element_id):
    timeout = 10
    timeout_messege = f"Element o id {element_id} nie pojawil sie w czasie {timeout} s."
    lokalizator = ("id", element_id) #szukanie po id konkretnej wartości
    znaleziono = excon.visibility_of_element_located(lokalizator) #patyk do dzigania strony
    #obiekt bedzie pytany czy jest OK, odpowiedź (T/F) zalezy od tego czy jest widoczny
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_messege)


driver = webdriver.Chrome()
driver.get("http://www.saucedemo.com")
try:
    login_button = czekaj_na_id("login-button")
except:






make_screenshot(driver)
time.sleep(2)
driver.quit()