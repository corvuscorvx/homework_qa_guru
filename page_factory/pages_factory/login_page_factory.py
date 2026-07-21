from seleniumpagefactory.Pagefactory import PageFactory
from selenium.common.exceptions import TimeoutException


class LoginPageFactory(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.locators = {
            "login_input": ("CSS", "#login-input"),
            "password_input": ("CSS", "#password-input"),
            "login_button": ("CSS", "#submit-button"),
            "error_message_output": ("CSS", "#error-message")
        }

    def input_login(self, login: str = None):
        if login is not None:
            self.login_input.send_keys(login)

    def input_password(self, password: str = None):
        if password is not None:
            self.password_input.send_keys(password)

    def click_login_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.login_button)
        self.login_button.click()

    def get_error_message(self, error_message: str) -> bool:

        try:
            self.error_message_output.visibility_of_element_located()
            actual_error_message = self.error_message_output.text
            return actual_error_message == error_message

        except TimeoutException:
            return False
