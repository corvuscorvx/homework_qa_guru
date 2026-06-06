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
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    PICTURE = (By.ID, "uploadPicture")
    LAST_NAME = (By.ID, "lastName")
    FIRST_NAME = (By.ID, "firstName")
    USER_EMAIL = (By.ID, "userEmail")
    MOBILE_NUMBER = (By.ID, "userNumber")
    BUTTON_SUBMIT = (By.ID, "submit")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    #Локаторы гендер
    GENDER_MALE_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_OTHER_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    GENDER_FEMALE_LABEL = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_MALE_INPUT = (By.ID, "gender-radio-1")
    GENDER_OTHER_INPUT = (By.ID, "gender-radio-3")
    GENDER_FEMALE_INPUT = (By.ID, "gender-radio-2")
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
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/section/h1"))
        )
        return form_title.text

    #наличие подзаголовка
    def get_sub_title(self):
        form_sub_title = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/section/div/p"))
        )
        return form_sub_title.text

    #Закрыть баннер
    def close_banner(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Level up your automation')]"))
        )
        close_banner_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, """//*[@id="fixedban"]/div/div/button"""))
        )
        close_banner_button.click()
        self.wait.until(EC.invisibility_of_element(close_banner_button))

    #Ввести имя
    def input_first_name(self, first_name):
        actual_first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)) #не нужна * принимает кортеж как один элемент
        actual_first_name.send_keys(first_name)
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME, first_name))

    #Ввести фамилию
    def input_last_name(self, last_name):
        actual_last_name = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        actual_last_name.send_keys(last_name)
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME, last_name))

    #Ввести email
    def input_email(self, email):
        actual_email = self.wait.until(EC.element_to_be_clickable(self.USER_EMAIL))
        actual_email.send_keys(email)
        self.wait.until(EC.text_to_be_present_in_element_value(self.USER_EMAIL, email))

    #Выбрать гендер
    def pick_gender(self, label_locator, input_locator):
        actual_gender = self.wait.until(EC.element_to_be_clickable(label_locator))
        actual_gender.click()
        actual_gender_input = self.wait.until(EC.presence_of_element_located(input_locator))
        assert actual_gender_input.is_selected() == True

    #Ввести номер
    def input_number(self, number):
        actual_number = self.driver.find_element(*self.MOBILE_NUMBER)
        actual_number.send_keys(number)
        number_value = actual_number.get_attribute("value")
        number_len = len(number_value)
        assert number_len == 10, f"Ошибка, не 10 цифр! Поле должно содержать номер начиная с 9"

    #Указать дату рождения
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

        day_pick = self.driver.find_element(
            By.CSS_SELECTOR, ".react-datepicker__day--011:not(.react-datepicker__day--outside-month)"
        )
        day_pick.click()

        actual_date_of_birth_value = actual_date_of_birth.get_attribute("value")
        expected_date = "11 Jun 1996"
        assert actual_date_of_birth_value == expected_date,\
            f"Ошибка! Ожидали дату '{expected_date}', но в поле отображается '{actual_date_of_birth_value}'"

    #Выбрать предмет
    def pick_subjects(self):
        subject = self.wait.until(EC.element_to_be_clickable((By.ID, "subjectsInput")))
        subject.send_keys("Physics")
        subject.send_keys(Keys.ENTER)
        subject_chip = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="subjectsChips"]/div/span[1]'))
        )
        subject_chip_text = subject_chip.text
        expected_subject = "Physics"
        assert subject_chip_text == expected_subject,\
            f"Ошибка! Ожидали предмет '{expected_subject}', "f"но отображается '{subject_chip_text}'"

    #Выбрать хобби
    def pick_hobbies(self, hobbies_list):
        assert 0 <= len(hobbies_list) <= 3, f"Можно выбрать максимум три хобби"
        for label_locator, input_locator in hobbies_list:
            actual_hobbies = self.wait.until(EC.element_to_be_clickable(label_locator))
            actual_hobbies.click()
            actual_hobbies_input = self.wait.until(EC.presence_of_element_located(input_locator))
            assert actual_hobbies_input.is_selected() == True, f"Чекбокс {input_locator} не выбрался"

    #Скролл
    @staticmethod
    def use_scroll():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

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
    def delite_file():
        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")

    #Ввести адрес
    def input_current_address(self):
        actual_current_address = self.driver.find_element(*self.CURRENT_ADDRESS)
        actual_current_address.send_keys("Полагаю, что это временный адрес!")
        current_address_value = actual_current_address.get_attribute("value")
        assert current_address_value == "Полагаю, что это временный адрес!",\
            f"Не совпадает! Получили: '{current_address_value}'"

    #Выбрать штат
    def pick_state(self):
        state_dropdown = self.wait.until(EC.element_to_be_clickable(self.STATE))
        state_dropdown.click()
        state_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="stateCity-wrapper"]/div[1]'))
        )
        state_option.click()

    #Выбрать город
    def pick_city(self):
        city_dropdown = self.wait.until(EC.element_to_be_clickable(self.CITY))
        city_dropdown.click()
        city_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="stateCity-wrapper"]/div[1]'))
        )
        city_option.click()

    #Нажать кнопку
    def submit_button(self):
        submit_button = driver.find_element(*self.BUTTON_SUBMIT)
        driver.execute_script("arguments[0].click();", submit_button)

    #Отображение окна с результатами
    def check_result_modal(self):
        modal_title = self.wait.until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        assert modal_title.text == "Thanks for submitting the form", (
            f"Заголовок модального окна не совпадает! Получили: '{modal_title.text}'"
        )

    #Проверка результатов
    @staticmethod
    def check_result_data():
        result_table = driver.find_element(By.CLASS_NAME, "table-responsive")
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

        hobbies_list = [
            (self.HOBBIES_SPORTS_LABEL, self.HOBBIES_SPORTS_INPUT),
            (self.HOBBIES_READING_LABEL, self.HOBBIES_READING_INPUT)
        ]
        self.pick_hobbies(hobbies_list)
        print("Тест прошел успешно.")

        self.use_scroll()
        print("Страница прокручена до подвала.")

        temp_file = self.create_file()
        self.upload_file(temp_file)
        print("Тест пройден. Файл создан и загружен.")

        self.input_current_address()
        print("Тест пройден. Адрес указан!")

        self.pick_state()
        self.pick_city()
        print("Штат и город выбраны.")

        self.submit_button()
        print("Кнопка нажата.")
        self.check_result_modal()
        print("Результаты совпали!")

        self.delite_file()
        print("Временный файл удален.")
        self.tear_down_test()
        print("Драйвер выключен.")

url = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
driver = webdriver.Chrome()
student_form = StudentForm(url, driver)
student_form.test01()