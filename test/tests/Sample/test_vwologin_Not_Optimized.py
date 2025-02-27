import time

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from test.util.Utils import *
from dotenv import load_dotenv
import os

@allure.title("VWO Negitive Test cases")
@allure.description("TC1 - Negitive Test cases - VWO login with invalid cred")
@allure.feature("VWO login with invalid cred")
@pytest.mark.negitivevwologin

def test_app_vwo_login_chrome():
    load_dotenv()
    match os.getenv("BROWSER"):
       case "chrome":
           chrome_option = Options()
           chrome_option.add_argument("--incognito")
           driver = webdriver.Chrome(options=chrome_option)

       case "edge":
           edge_option = Options()
           edge_option.add_argument("--inprivate")
           driver = webdriver.Edge(options=edge_option)


       case "firefox":
           firefox_option = Options()
           firefox_option.add_argument("-privagte")
           driver = webdriver.Firefox(options=firefox_option)

       case _:
           print("Browser Not found")
           exit(1)

    driver.get(os.getenv("URL"))

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys(os.getenv("INVALID_EMAIL"))

    password_web_element = driver.find_element(By.ID, "login-password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    time.sleep(3)
    error_messeage_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_messeage_web_element.text)

    take_screen_shot(driver=driver,name="vwologin")

    assert error_messeage_web_element.text == os.getenv("error_message_expected")
    driver.quit()




