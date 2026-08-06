from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_factory.pages_factory.elements.calendar_pf import Calendar
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class RegistrationPageFactory(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        super().__init__()
        self.calendar = Calendar(driver)
        self.locators = {
            "file_input": ("CSS", "#uploadPicture"),
            "city_input": ("CSS", "#city"),
            "state_input": ("CSS", "#state"),
            "email_input": ("CSS", "#userEmail"),
            "number_input": ("CSS", "#userNumber"),
            "submit_button": ("CSS", "#submit"),
            "city_dropdown": ("CSS", "#stateCity-wrapper"),
            "state_dropdown": ("CSS", "#stateCity-wrapper"),
            "subjects_input": ("CSS", "#subjectsInput"),
            "last_name_input": ("CSS", "#lastName"),
            "first_name_input": ("CSS", "#firstName"),
            "gender_male_radio": ("CSS", "label[for='gender-radio-1']"),
            "gender_other_radio": ("CSS", "label[for='gender-radio-3']"),
            "error_message_area": ("CSS", "#formError"),
            "gender_female_radio": ("CSS", "label[for='gender-radio-2']"),
            "date_of_birth_input": ("CSS", "#dateOfBirthInput"),
            "modal_dialog_result": ("CSS", "#resultBody"),
            "hobby_music_checkbox": ("CSS", "label[for='hobbies-checkbox-3']"),
            "current_address_input": ("CSS", "#currentAddress"),
            "hobby_sports_checkbox": ("CSS", "label[for='hobbies-checkbox-1']"),
            "hobby_reading_checkbox": ("CSS", "label[for='hobbies-checkbox-2']")
        }

    def close_banner(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']"))
        ).click()

    def input_first_name(self, first_name: str = None):
        if first_name is not None:
            self.first_name_input.send_keys(first_name)

    def input_last_name(self, last_name: str = None):
        if last_name is not None:
            self.last_name_input.send_keys(last_name)

    def input_email(self, email: str = None):
        if email is not None:
            self.email_input.send_keys(email)

    def select_gender(self, gender: str = None):
        if gender:
            gender_formatted = gender.capitalize()

            gender_map = {
                "Male": self.gender_male_radio,
                "Female": self.gender_female_radio,
                "Other": self.gender_other_radio
            }

            gender_map[gender_formatted].click()

    def input_number(self, number: str = None):
        if number is not None:
            self.number_input.send_keys(number)

    def select_date_of_birth(self, day: int, month: int, year: int):
        self.date_of_birth_input.click()
        self.calendar.select_date(day, month, year)

    def input_subjects(self, subjects: list[str] | str = None) -> str | None:
        if subjects is not None:
            subjects_list = subjects if isinstance(subjects, list) else [subjects]
            self.subjects_input.element_to_be_clickable()

            for subject in subjects_list:
                self.subjects_input.send_keys(subject)
                self.subjects_input.send_keys(Keys.ENTER)

            self.driver.execute_script("arguments[0].blur();", self.subjects_input)
            return ", ".join(subjects_list)
        return None

    def select_hobbies(self, hobbies: list[str] | str = None) -> list | None:

        if hobbies is not None:
            hobbies_list = hobbies if isinstance(hobbies, list) else [hobbies]
            result_list = []

            for hobby in hobbies_list:
                hobby_formatted = hobby.capitalize()

                if hobby_formatted == "Sports":
                    self.hobby_sports_checkbox.click_button()
                elif hobby_formatted == "Reading":
                    self.hobby_reading_checkbox.click_button()
                elif hobby_formatted == "Music":
                    self.hobby_music_checkbox.click_button()

                result_list.append(hobby_formatted)
            return result_list
        return None

    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

    def upload_file(self, file_path: str):
        self.file_input.element_to_be_clickable()
        self.file_input.send_keys(file_path)

    def input_current_address(self, current_address: str = None):
        if current_address is not None:
            self.current_address_input.send_keys(current_address)

    def select_state(self, state_name: str):
        if state_name is not None:
            state_option_xpath = f"//div[@class='state-city-option' and text()='{state_name}']"
            self.state_input.click()
            self.state_dropdown.visibility_of_element_located()

            state = self.driver.find_element(By.XPATH, state_option_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", state)
            self.driver.execute_script("arguments[0].click();", state)

    def get_expected_birth_date_text(self, day: int, month: int, year: int) -> str:
        return self.calendar.format_to_site_date(day, month, year)

    def select_city(self, city_name: str):
        if city_name is not None:
            city_option_xpath = f"//div[@class='state-city-option' and text()='{city_name}']"
            self.city_input.click()
            self.city_dropdown.visibility_of_element_located()

            city = self.driver.find_element(By.XPATH, city_option_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", city)
            self.driver.execute_script("arguments[0].click();", city)

    def click_submit_button(self):
        self.submit_button.click()

    def get_result_form(self) -> str:
        self.modal_dialog_result.visibility_of_element_located()
        return self.modal_dialog_result.text

    def get_error_message(self):
        self.error_message_area.visibility_of_element_located()
        return self.error_message_area.text
