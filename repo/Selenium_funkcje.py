import datetime


def make_screenshot(driver, nazwa):
    teraz = datetime.datetime.now()
    screenshot = nazwa + teraz.strftime('%d_%b_%y_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)


