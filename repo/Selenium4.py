from selenium import webdriver

class LoginPage:
    def __init__(self, driver, user="user-name", passwd="secret_sauce", login_button="login-button"):
        self.driver = driver
        self.username_field = user
        self.password_field = passwd
        self.login_button = login_button


    def open(self):
        self.driver.get("http://www.saucedemo.com")


    def enter_username(self, username_tresc):
        field = self.driver.find_element("id", self.username_field)
        field.clear()
        field.send_keys(username_tresc)


    def password(self, password_tresc):
        field = self.driver.find_element("id", self.password_field)
        field.clear()
        field.send_keys(password_tresc)


    def click_login_button(self):
        field = self.driver.find_element("id", self.login_button )
        field.click()