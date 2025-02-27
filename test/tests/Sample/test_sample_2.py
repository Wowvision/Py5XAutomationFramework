import pytest
import allure
import time

from selenium import webdriver
@allure.title("Dry run of the framework 1")
@allure.description("Verify that dry run is working 1")
@allure.feature("TC0 : Sample Test run")
@pytest.mark.sample

def test_sample_pass():
    print("Hello sample")
    assert True == True


@allure.title("Dry run of the framework 2")
@allure.description("Verify that dry run is working 2")
@allure.feature("TC1 : Sample Failed run")
@pytest.mark.sample

def test_sample_failed():
    print("Hello sample")
    assert True == False

