import allure
import pytest
import time

from selenium import webdriver
from tests.selenium_unitest import LoginPage

#Assertion and use the page object class

#Webdriver start
#User interation + Assertion
#Close driver

from test.constants.constants import Constant

from test.pageObjects.PageObjectModel.VWO.dashboardPage import DashboardPage
from test.pageObjects.PageObjectModel.VWO.loginPage import LoginPage
from test.pageObjects.PageObjectModel.VWO.freeTrialpage import FreeTrialPage

@allure.title("VWO Login Test")
@allure.description("TC0 - VWO negitive test case")
@allure.feature("feature Negitive test case")
@pytest.mark.negitive

def test_vwo_negitive():
    driver = webdriver.Chrome()
    driver.get(Constant.app_url())
    loginPage = LoginPage(driver=driver)
    loginPage.login_to_vwo(usr="admin@1234",pwd="123")
    error_mes_element = loginPage.get_error_message_text()
    assert error_mes_element == "Your email, password, IP address or location did not match"


