import time
import os
import unittest
from operator import truediv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StudentForm:


    LAST_NAME = (By.ID, "lastName")
    FIRST_NAME = (By.ID, "firstName")
    USER_EMAIL = (By.ID, "userEmail")
    MOBILE_NUMBER = (By.ID, "userNumber")

    GENDER_MALE_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_OTHER_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    GENDER_FEMALE_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_MALE_INPUT = (By.ID, "gender-radio-1")
    GENDER_OTHER_INPUT = (By.ID, "gender-radio-3")
    GENDER_FEMALE_INPUT = (By.ID, "gender-radio-2")

    # HOBBIES_READING = (By.ID, "hobbies-checkbox-2")
    # SUBJECTS_DROPDOWN = (By.ID, "subjectsDropdown")
    # CURRENT_ADDRESS = (By.ID, "currentAddress")
    # BUTTON_SUBMIT = (By.ID, "submit")
    # STATE = (By.ID, "state")
    # PICTURE = (By.ID, "uploadPicture")

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.default_timeout = 10
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    def set_driver(self, driver):
        self.driver = driver

    def set_up_test(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    def tear_down_test(self):
        self.driver.quit()

    def get_title(self): #наличие заголовка
        form_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/section/h1")))
        return form_title.text

    def get_sub_title(self): #наличие подзаголовка
        form_sub_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/section/div/p")))
        return form_sub_title.text

    def close_banner(self): #закрытие баннера
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Level up your automation')]")))
        close_banner_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="fixedban"]/div/div/button""")))
        close_banner_button.click()
        self.wait.until(EC.invisibility_of_element(close_banner_button))

    def input_first_name(self, first_name):
        actual_first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)) #не нужна * принимает кортеж как один элемент
        actual_first_name.send_keys(first_name)
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME, first_name))
    def input_last_name(self, last_name):
        actual_last_name = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        actual_last_name.send_keys(last_name)
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME, last_name))

    def input_email(self, email):
        actual_email = self.wait.until(EC.element_to_be_clickable(self.USER_EMAIL))
        actual_email.send_keys(email)
        self.wait.until(EC.text_to_be_present_in_element_value(self.USER_EMAIL, email))

    def pick_gender(self, label_locator, input_locator):
        actual_gender = self.wait.until(EC.element_to_be_clickable(label_locator))
        actual_gender.click()
        actual_gender_input = self.wait.until(EC.presence_of_element_located(input_locator))
        assert actual_gender_input.is_selected() == True

    def input_number(self, number):
        actual_number = self.driver.find_element(*self.MOBILE_NUMBER)
        actual_number.send_keys(number)
        number_value = actual_number.get_attribute("value")
        number_len = len(number_value)
        assert number_len == 10, f"Ошибка, не 10 цифр! Поле должно содержать номер начиная с 9"

    def pick_date_of_birth(self):
        actual_date_of_birth = self.driver.find_element(By.ID, "dateOfBirthInput")
        actual_date_of_birth.click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))

        year_pick = self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_pick.click()
        year_pick.find_element(By.XPATH, "//option[@value='1996']").click()

        month_pick = self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        month_pick.click()
        month_pick.find_element(By.XPATH, "//option[text()='June']").click()

        day_pick = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--011:not(.react-datepicker__day--outside-month)")
        day_pick.click()

        actual_date_of_birth_value = actual_date_of_birth.get_attribute("value")
        expected_date = "11 Jun 1996"
        assert actual_date_of_birth_value == expected_date, f"Ошибка! Ожидали дату '{expected_date}', но в поле отображается '{actual_date_of_birth_value}'"

    def pick_subjects(self):
        subject = self.wait.until(EC.element_to_be_clickable((By.ID, "subjectsInput")))
        subject.send_keys("Physics")
        subject.send_keys(Keys.ENTER)
        subject_chip = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="subjectsChips"]/div/span[1]')))
        subject_chip_text = subject_chip.text
        expected_subject = "Physics"
        assert subject_chip_text == expected_subject, f"Ошибка! Ожидали предмет '{expected_subject}', "f"но отображается '{subject_chip_text}'"


    def test01(self):
        self.set_up_test()

        actual_title = self.get_title()
        assert actual_title == "Practice Form", f"Ожидали 'Practice Form', но получили '{actual_title}'"

        actual_sub_title = self.get_sub_title()
        assert actual_sub_title == "Student Registration Form", f"Ожидали 'Student Registration Form', но получили '{actual_sub_title}'"
        print("Тест успешно пройден! Заголовок и подзаголовок совпадают.")

        self.close_banner()
        print("Тест успешно пройден, окно закрыто!")

        self.input_first_name("Автомат")
        self.input_last_name("Автоматов")
        print("Тест успешно пройден, Имя и Фамилия заполнены")

        self.input_email("Avtomat@pitonov.com")
        print("Тест успешно пройден, email заполнен!")

        self.pick_gender(self.GENDER_FEMALE_LABEL, self.GENDER_FEMALE_INPUT)
        print("Тест пройден, гендер выбран!")

        self.input_number("9123456780")
        print("Тест пройден, в поле 10 цифр")

        self.pick_date_of_birth()
        print("Тест прошел успешно!")

        self.pick_subjects()
        print("Тест прошел успешно!")

        self.pick_subjects()
        print("Тест прошел успешно.")

url = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
driver = webdriver.Chrome()
student_form = StudentForm(url, driver)
student_form.test01()

# def get_email(self, email):
#     self.driver.find_element(*self.USER_EMAIL).send_keys(email)
#
# def get_picture(self, upload_picture):
#     self.driver.find_element(*self.PICTURE).send_keys(upload_picture)
#
# def get_mobile_number(self, mobile_number):
#     self.driver.find_element(*self.MOBILE_NUMBER).send_keys(mobile_number)
#
# def get_current_address(self, current_address):
#     self.driver.find_element(*self.CURRENT_ADDRESS).send_keys(current_address)
#
# def get_date_of_birth(self):
#
#     self.driver.find_element(*self.DATE_BIRTH).click()
# def get_subjects(self):
#     self.driver.find_element(*self.SUBJECTS_DROPDOWN).click()
#
# def get_gender_male(self):
#     self.driver.find_elements(*self.GENDER_MALE).click()
# def get_gender_other(self):
#     self.driver.find_elements(*self.GENDER_OTHER).click()
# def get_gender_female(self):
#     self.driver.find_elements(*self.GENDER_FEMALE).click()
#
# def get_hobbies_sport(self):
#     self.driver.find_element(*self.HOBBIES_SPORT).click()
# def get_hobbies_music(self):
#     self.driver.find_element(*self.HOBBIES_MUSIC).click()
# def get_hobbies_reading(self):
#     self.driver.find_element(*self.HOBBIES_READING).click()
#
# def get_state(self):
#     self.driver.find_element(*self.STATE).click()
#
# def get_submit_button(self):
#     self.driver.find_element(*self.BUTTON_SUBMIT).click()


# def __init__(self, firstName, lastName, gender, user_number):
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.gender = gender
    #     self.user_number = user_number

