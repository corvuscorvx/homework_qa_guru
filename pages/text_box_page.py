from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    OUTPUT_AREA = (By.CSS_SELECTOR, "#output")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")

    def input_full_name(self, full_name):
        self.input_text(self.FULL_NAME, full_name)

    def input_email(self, email):
        self.input_text(self.EMAIL, email)

    def input_current_address(self, current_address):
        self.input_text(self.CURRENT_ADDRESS, current_address)

    def input_permanent_address(self, permanent_address):
        self.input_text(self.PERMANENT_ADDRESS, permanent_address)

    def click_submit_button(self):
        self.click_element(self.SUBMIT_BUTTON)

    def get_actual_data(self):
        return self.get_element_text(self.OUTPUT_AREA)

    def get_email_validation_message(self):
        return self.get_validation_message(self.EMAIL)
