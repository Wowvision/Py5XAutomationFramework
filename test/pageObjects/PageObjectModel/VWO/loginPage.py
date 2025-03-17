import time

from selenium.webdriver.common.by import By

from test.util.Common_utils import web_driver_wait


class LoginPage:

    def __init__(self,driver):
        self.driver= driver

    #Page Locators
    username=(By.ID,"login-username")
    password =(By.NAME,"password")
    submit_button =(By.XPATH,"//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    #Page Action
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)  #Syntax to return the element


    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        web_driver_wait(driver=self.driver, element_tuple=self.error_message,timeout=5)
        return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self,usr,pwd):
        try:
            self.get_username().sendkeys(usr)
            self.get_password().sendkeys(pwd)
            self.get_submit_button().click

        except Exception as e:
            print(e)

    def get_error_message_text(self):
        return self.get_error_message().text





