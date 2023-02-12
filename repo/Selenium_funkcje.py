import datetime
import time

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)


# def make_screenshot(driver):
#     teraz = datetime.datetime.now()
#     screenshot = "ss" + teraz.strftime("_%d-%b-%y-%H%M%S") + ".png"
#     driver.get_screenshot_as_file(screenshot)
