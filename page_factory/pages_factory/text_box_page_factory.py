from seleniumpagefactory.Pagefactory import PageFactory
from seleniumpagefactory.Pagefactory import ElementNotVisibleException


class TextBoxPageFactory(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.locators = {
            "email_input": ("CSS", "#userEmail"),
            "output_area": ("CSS", "#output"),
            "output_email": ("CSS", "#output #email"),
            "submit_button": ("CSS", "#submit"),
            "full_name_input": ("CSS", "#userName"),
            "output_full_name": ("CSS", "#output #name"),
            "current_address_input": ("CSS", "#currentAddress"),
            "output_current_address": ("CSS", "#output #currentAddress"),
            "permanent_address_input": ("CSS", "#permanentAddress"),
            "output_permanent_address": ("CSS", "#output #permanentAddress")
        }

    def input_full_name(self, full_name: str = None):
        if full_name is not None:
            self.full_name_input.send_keys(full_name)

    def input_email(self, email: str = None):
        if email is not None:
            self.email_input.send_keys(email)

    def input_current_address(self, current_address: str = None):
        if current_address is not None:
            self.current_address_input.send_keys(current_address)

    def input_permanent_address(self, permanent_address: str = None):
        if permanent_address is not None:
            self.permanent_address_input.send_keys(permanent_address)

    def click_submit_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.submit_button)
        self.submit_button.click()

    def get_output_data(self):
        try:
            if not self.output_area or not self.output_area.is_displayed():
                return None

            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.output_area)

            full_name = self.output_full_name.text.replace("Name:", "").strip()
            email = self.output_email.text.replace("Email:", "").strip()
            current_address = self.output_current_address.text.replace("Current Address :", "").strip()
            permanent_address = self.output_permanent_address.text.replace("Permananet Address :", "").strip()

            return {
                "full_name": full_name,
                "email": email,
                "current_address": current_address,
                "permanent_address": permanent_address
            }
        except ElementNotVisibleException:
            return None

    def is_email_error_present(self):
        is_valid = self.driver.execute_script("return arguments[0].checkValidity();", self.email_input)
        return not is_valid

    def get_email_validation_message(self):
        return self.email_input.get_attribute("validationMessage")
