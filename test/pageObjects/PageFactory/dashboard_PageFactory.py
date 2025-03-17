from seleniumpagefactory.Pagefactory import PageFactory
import time
from test.util.Common_utils import *

class DashboardPage(PageFactory):

    def __init__(self,driver):
        self.driver = driver
        self.highlight=True

    locators = {
        'username_logged_in' :('XPATH', "//span[@data-qa='lufexuloga']")

    }

    def user_logged_in_text(self):
        webdriver_wait_url(driver=self.driver,timeout=10)
        return self.username_logged_in.get_text()


