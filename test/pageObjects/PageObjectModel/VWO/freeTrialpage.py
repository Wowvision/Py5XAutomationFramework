from selenium.webdriver.common.by import By
from test.util.Common_utils import web_driver_wait

class FreeTrialPage:

    def __init__(self,driver):
        self.driver = driver

    start_a_free_trial = (By.XPATH,"//a[@data-qa='bericafeqo']")
    username_email_ft = (By.ID,"//input[@id='page-v1-step1-email']")
    button_click_ft = (By.XPATH,"//button[normalize-space()='Create a Free Trial Account']")
    checkbox_terms = (By.XPATH,"//input[@id='page-free-trial-step1-cu-gdpr-consent-checkbox']")
    error_message_invalid_email = (By.XPATH,"//div[normalize-space()='The email address you entered is incorrect.']")


    def get_user_name_ft(self):
        return self.driver.find_element(*FreeTrialPage.username_email_ft)


    def get_button_click_ft(self):
        return self.driver.find_element(*FreeTrialPage.button_click_ft)

    def get_button_checkbox_terms(self):
        return self.driver.find_element(*FreeTrialPage.checkbox_terms)

    def get_start_free_trial_link_text(self):
        return self.driver.find_element(*FreeTrialPage.start_a_free_trial)

    def get_error_message(self):
        return self.driver.find_element(*FreeTrialPage.error_message_invalid_email)

    def get_error_mess_text(self):
        return self.get_error_message().text

    def enter_free_trial_details_invalid(self,invlaid_usrname):
        try:
            self.get_user_name_ft().sendkeys(invlaid_usrname)
            self.get_button_checkbox_terms().click
            self.get_button_click_ft()

        except Exception as e:
            print(e)



