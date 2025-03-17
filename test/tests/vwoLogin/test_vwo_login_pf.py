import logging

import allure
from selenium import webdriver

import pytest
import selenium
import time
import logging

from test.constants.constants import Constant
from test.pageObjects.PageFactory.dashboard_PageFactory import DashboardPage
from test.pageObjects.PageFactory.loginPage_PageFactory import LoginPage
from allure_commons.types import AttachmentType

from test.tests.vwoLogin.conftest import setup


@allure.epic("VWO login")
@allure.feature("Login test")
class TestVWOLogin():
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negitive(self,setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver= setup
            driver.get(Constant.app_url())
            loginpage = LoginPage(driver)
            loginpage.login_to_vwo(usr=self.username,pwd=123)
            error_message = loginpage.error_msg()
            assert error_message == "Your email, password, IP address or location did not match"

        except Exception as e:
            print(e)

    def test_vwo_login_positive(self, setup):
            driver = setup
            driver.get(Constant.app_url())
            loginpage = LoginPage(driver)
            loginpage.login_to_vwo(usr=self.username, pwd=self.password)
            dashboardPage = DashboardPage(driver)
            username = dashboardPage.user_logged_in_text()
            assert "mannu goel" ==username




