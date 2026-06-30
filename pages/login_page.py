from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    URL = "https://qa-guru.github.io/one-page-form/login.html"

    LOGIN = (By.CSS_SELECTOR, "#login-input")
    PASSWORD = (By.CSS_SELECTOR, "#password-input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit-button")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "#error-message")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.open_url(self.URL)
        self.input_text(self.LOGIN, username)
        self.input_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)