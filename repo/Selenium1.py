from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
print("Nazwa strony:", driver.title)
button1_accept = driver.find_element("id", "L2AGLb")
button1_accept.click()
print(button1_accept)
pole_szukaj = driver.find_element(By.NAME("q"))
print(pole_szukaj)
time.sleep(500)
driver.quit()


# <button id="L2AGLb" class="tHlp8d" data-ved="0ahUKEwi2r_eSwI39AhVIh_0HHXC8DOIQiZAHCB8"><div class="QS5gu sy4vM" role="none">Zaakceptuj wszystko</div></button>