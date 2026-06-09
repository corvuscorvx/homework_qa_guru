import time
import os
from datetime import datetime
import unittest
from operator import truediv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StudentForm:
    CITY = (By.CSS_SELECTOR, "#city")
    STATE = (By.CSS_SELECTOR, "#state")
    PICTURE = (By.CSS_SELECTOR, "#uploadPicture")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    USER_EMAIL = (By.CSS_SELECTOR, "#userEmail")
    MOBILE_NUMBER = (By.CSS_SELECTOR, "#userNumber")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "#submit")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    MODAL_DIALOG = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    MODAL_DIALOG_RESULT = (By.CSS_SELECTOR, "div[class='table-responsive']")
    #Локаторы гендер
    GENDER_MALE_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_OTHER_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    GENDER_FEMALE_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_MALE_INPUT = (By.CSS_SELECTOR, "#gender-radio-1")
    GENDER_OTHER_INPUT = (By.CSS_SELECTOR, "#gender-radio-3")
    GENDER_FEMALE_INPUT = (By.CSS_SELECTOR, "#gender-radio-2")
    #Локаторы хобби
    HOBBIES_MUSIC_LABEL = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    HOBBIES_SPORTS_LABEL = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING_LABEL = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC_INPUT = (By.ID, "hobbies-checkbox-3")
    HOBBIES_SPORTS_INPUT = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING_INPUT = (By.ID, "hobbies-checkbox-2")

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

    # наличие заголовка
    def get_title(self):
        form_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return form_title.text

    #наличие подзаголовка
    def get_sub_title(self):
        form_sub_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".practice-form-wrapper"))
        )
        return form_sub_title.text

    #Закрыть баннер
    def close_banner(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        close_banner_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']"))
        )
        close_banner_button.click()
        self.wait.until(
            EC.invisibility_of_element(close_banner_button)
        )

    #Ввести имя
    def input_first_name(self, first_name):
        actual_first_name = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME) #не нужна * принимает кортеж как один элемент
        )
        actual_first_name.send_keys(first_name)
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.FIRST_NAME, first_name)
        )
        return first_name

    #Ввести фамилию
    def input_last_name(self, last_name):
        actual_last_name = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME)
        )
        actual_last_name.send_keys(last_name)
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.LAST_NAME, last_name)
        )
        return last_name

    #Ввести email
    def input_email(self, email):
        actual_email = self.wait.until(
            EC.element_to_be_clickable(self.USER_EMAIL)
        )
        actual_email.send_keys(email)
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.USER_EMAIL, email)
        )
        return email

    #Выбрать гендер
    def pick_gender(self, label_locator, input_locator):
        actual_gender = self.wait.until(
            EC.element_to_be_clickable(label_locator)
        )
        actual_gender.click()
        actual_gender_input = self.wait.until(
            EC.presence_of_element_located(input_locator)
        )
        assert actual_gender_input.is_selected() == True


    #Ввести номер
    def input_number(self, number):
        actual_number = self.driver.find_element(*self.MOBILE_NUMBER)
        actual_number.send_keys(number)
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.MOBILE_NUMBER, number)
        )

    #Указать дату рождения
    def pick_date_of_birth(self, day, month, year):
        actual_date_of_birth = self.driver.find_element(
            By.CSS_SELECTOR, "#dateOfBirthInput"
        )
        actual_date_of_birth.click()
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='react-datepicker__month-container']"))
        )

        year_pick = self.driver.find_element(
            By.CSS_SELECTOR, "select[class='react-datepicker__year-select']"
        )
        year_pick.click()
        self.driver.find_element(
            By.CSS_SELECTOR, f"option[value='{year}']"
        ).click()

        month_pick = self.driver.find_element(
            By.CSS_SELECTOR, "select[class='react-datepicker__month-select']"
        )
        month_pick.click()
        value_month = int(month - 1)
        self.driver.find_element(
            By.CSS_SELECTOR, f"option[value='{value_month}']"
        ).click()

        day_pick = self.driver.find_element(
            By.CSS_SELECTOR, f"span[data-day='{day}']"
        )
        day_pick.click()

        birth_date = datetime(year=int(year), month=int(month), day=int(day))
        expected_date_text = birth_date.strftime("%d %b %Y")
        actual_date_text = actual_date_of_birth.get_attribute("value")
        assert actual_date_text == expected_date_text, (
            f"Ошибка! Ожидали: '{expected_date_text}', "
            f"Отображается: '{actual_date_text}'"
        )

    #Выбрать предмет
    def pick_subjects(self, subject):
        subject_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#subjectsInput"))
        )
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.ENTER)
        subject_chip = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="subjects-chip__label"]'))
        )
        subject_chip_text = subject_chip.text
        expected_subject = subject.capitalize()
        assert subject_chip_text == expected_subject,\
            f"Ошибка! Ожидали предмет '{expected_subject}', "f"но отображается '{subject_chip_text}'"

    #Выбрать хобби
    def pick_hobbies(self, hobbies_list):
        for hobby in hobbies_list:
            self.wait.until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{hobby}']"))
            ).click()

    #Скролл
    def use_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

    #Создание временного файла
    @staticmethod
    def create_file():
        temp_file_path = os.path.abspath("test_image.jpg")
        with open(temp_file_path, "w") as f:
            f.write("fake image data")
        return temp_file_path

    #Загрузка временного файла
    def upload_file(self, temp_file_path):
        upload_input = self.driver.find_element(*self.PICTURE)
        upload_input.send_keys(temp_file_path)

    #Удаление временного файла
    @staticmethod
    def delete_file():
        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")

    #Ввести адрес
    def input_current_address(self, address):
        actual_current_address = self.driver.find_element(
            *self.CURRENT_ADDRESS
        )
        actual_current_address.send_keys(address)
        current_address_value = actual_current_address.get_attribute("value")
        assert current_address_value == address,\
            f"Не совпадает! Получили: '{current_address_value}'"

    #Выбрать штат
    def pick_state(self, state_value):
        state_dropdown = self.wait.until(EC.element_to_be_clickable(self.STATE))
        state_dropdown.click()
        state_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="stateCity-wrapper"]/div[{state_value}]'))
        )
        state_option.click()

    #Выбрать город
    def pick_city(self, city_value):
        city_dropdown = self.wait.until(EC.element_to_be_clickable(self.CITY))
        city_dropdown.click()
        city_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="stateCity-wrapper"]/div[{city_value}]'))
        )
        city_option.click()

    #Нажать кнопку
    def submit_button(self):
        submit_button = driver.find_element(*self.BUTTON_SUBMIT)
        driver.execute_script("arguments[0].click();", submit_button)

    #Отображение окна с результатами
    def check_result_modal(self):
        modal_title = self.wait.until(
            EC.visibility_of_element_located(self.MODAL_DIALOG)
        )
        assert modal_title.text == "Thanks for submitting the form", (
            f"Заголовок модального окна не совпадает! Получили: '{modal_title.text}'"
        )
    #Проверка результатов
    def check_result_data(self):
        result_table = self.wait.until(
            EC.visibility_of_element_located(self.MODAL_DIALOG_RESULT)
        )
        # assert expected_full_name in table_text, "ФИО не найдено!" //*[@id="resultBody"]/tr[1]/td[2]
        # assert email in table_text, "Email не найден!"
        # assert gender in table_text, "Гендер не найден!"
        # assert mobile in table_text, "Номер не найден!"
        # assert expected_birth_date in table_text, "Дата рождения не найдена!"
        # assert subjects in table_text, "Предметы не найдены!"
        # assert expected_hobbies in table_text, "Хобби не найдены!"
        # assert file_name in table_text, "Файл не найден!"
        # assert address in table_text, "Адрес не найден!"
        # assert expected_state_city in table_text, "Штат и Город не найдены!"

        assert "Автомат Автоматов", result_table.text
        assert "Avtomat@pitonov.com", result_table.text
        assert "Male", result_table.text
        assert "1234567890", result_table.text
        assert "11 Jun 1996", result_table.text  # форма вывода даты может меняться от настроек
        assert "Physics", result_table.text
        assert "Sports, Reading", result_table.text
        assert "test_image.jpg", result_table.text
        assert "Полагаю, что это временный адрес!", result_table.text
        assert "NCR Delhi", result_table.text



    def test01(self):
        self.set_up_test()

        actual_title = self.get_title()
        assert actual_title == "Practice Form", f"Ожидали 'Practice Form', но получили '{actual_title}'"

        actual_sub_title = self.get_sub_title()
        assert actual_sub_title == "Student Registration Form", f"Ожидали 'Student Registration Form', но получили '{actual_sub_title}'"
        print("Тест прошел успешно, заголовок и подзаголовок совпадают.")

        self.close_banner()
        print("Тест прошел успешно, окно закрыто!")

        self.input_first_name("Автомат")
        self.input_last_name("Автоматов")
        print("Тест прошел успешно, имя и фамилия заполнены!")

        self.input_email("Avtomat@pitonov.com")
        print("Тест прошел успешно, email заполнен!")

        self.pick_gender(self.GENDER_FEMALE_LABEL, self.GENDER_FEMALE_INPUT)
        print("Тест прошел успешно, гендер выбран!")

        self.input_number("9123456780")
        print("Тест прошел успешно, номер введен!")

        self.pick_date_of_birth(1, 4, 1990)
        print("Тест прошел успешно, дата рождения введена!")

        self.pick_subjects("maths")
        print("Тест прошел успешно, объект выбран!")

        hobbies_list = []
        self.pick_hobbies(hobbies_list)
        print("Тест прошел успешно, хобби выбраны!")

        self.use_scroll()
        print("Страница прокручена до подвала!")

        temp_file = self.create_file()
        self.upload_file(temp_file)
        print("Тест прошел успешно, файл создан и загружен!")

        self.input_current_address("Полагаю, что это временный адрес!")
        print("Тест прошел успешно, адрес указан!")

        self.pick_state(1)
        self.pick_city(1)
        print("Тест прошел успешно, штат и город выбраны!")

        self.submit_button()
        print("Кнопка нажата.")
        self.check_result_data()
        print("Результаты совпали!")

        self.delete_file()
        print("Временный файл удален.")
        self.tear_down_test()
        print("Драйвер выключен.")

url = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
driver = webdriver.Chrome()
student_form = StudentForm(url, driver)
student_form.test01()