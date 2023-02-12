import datetime

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = driver.title + teraz.strftime(" %d-%b-%y-%H%M%S") + ".png"
    driver.get_screenshot_as_file(screenshot)