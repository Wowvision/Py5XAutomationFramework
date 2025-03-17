from selenium import webdriver
import pytest
import allure

import os
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Chrome()

@pytest.fixture(scope='class')

def setup(request):
    driver.maximize_window()

    username= os.getenv("EMAIL_ADDRESS")
    password= os.getenv("PASSWORD")

    request.cls.driver=driver
    request.cls.username = username
    request.cls.password = password

    yield driver
    driver.quit()

