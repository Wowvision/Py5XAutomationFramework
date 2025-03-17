import allure
from aenum import constant
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test.constants.constants import Constant

def web_driver_wait(driver, element_tuple):

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located(element_tuple))


def web_driver_wait(driver, element_tuple,timeout):

    WebDriverWait(driver=driver, timeout=timeout).until(
        EC.visibility_of_element_located(element_tuple))

def webdriver_wait_url(driver,timeout):
    WebDriverWait(driver=driver,timeout=timeout).until(
        EC.url_changes(Constant.app_dashboard_url()))