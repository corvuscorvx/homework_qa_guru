import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSuite:
    full_name_locator = "userName"
    email_locator = "userEmail"
    current_address_locator = "currentAddress"
    permanent_address_locator = "permanentAddress"
    button_locator = "submit"
    result_area_locator = "output"
    url = "https://qa-guru.github.io/one-page-form/text-box.html"
    driver = None

    def __init__(self, url, driver):#Инициализация объекта класса (объект - набор тестов)
        self.__url = url #записывает урл где будут проходить какие-то тесты в приватную переменную
        self.__driver = driver #записывает драйвер браузера где будут проходить какие-то тесты в приватную переменную

    def get_url(self): #общий метод для объектов TestSuite - возвращает приватный урл для объекта
        return self.__url

    def get_driver(self): #общий метод для объектов TestSuite - возвращает драйвера для объекта
        return self.__driver
    def set_driver(self, driver): #общий метод для объектов TestSuite - позволяет изменить драйвера для объекта
        self.__driver = driver

    def set_up_test(self): #общий метод для объектов TestSuite - подготовка среды для каждого теста
        self.__driver = webdriver.Chrome()  #запускает новое окно браузера и перезаписывает приватную переменную, чтобы каждый тест открывался в новом окне
        self.get_driver().get(self.get_url()) #получает драйвер, получает урл и переходит к нему
        self.get_driver().maximize_window() #обращается к браузеру и разворачивает его на весь экран
        time.sleep(3)

    def tear_down_test(self): #общий метод закрытия и очистки браузера для объекта после завершения теста
        if self.__driver: #есть ли открытый браузер?
            self.get_driver().quit() #если есть, то полностью избавляемся от него

    def test_case_01(self):  # Тест 01 полное имя
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()
            #переменная = для объекта драйвер ищет элемент на странице по id для этого объекта
            full_name_filed = self.get_driver().find_element(By.ID, self.full_name_locator)
            full_name_filed.send_keys("Автомат Селениумов")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_area_locator)
            assert "Автомат Селениумов" in result_box.text
            print("Тест 01 успешно пройден")
        finally:
            self.tear_down_test()

    def test_case_02(self): #Тест 02 email
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()

            email_filed = self.get_driver().find_element(By.ID, self.email_locator)
            email_filed.send_keys("Pitonist@qaguru.school")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_area_locator)
            assert "Pitonist@qaguru.school" in result_box.text
            print("Тест 02 успешно пройден")
        finally:
            self.tear_down_test()

    def test_case_03(self): #Тест03 временный адрес
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()

            current_address_field = self.get_driver().find_element(By.ID, self.current_address_locator)
            current_address_field.send_keys("Улица Пушкина, дом Колотушкина")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_area_locator)

            assert "Улица Пушкина, дом Колотушкина" in result_box.text
            print("Тест 03 успешно пройден!")
        finally:
            self.tear_down_test()

    def test_case_04(self): #Тест04 постоянный адрес
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()

            permanent_address_filed = self.get_driver().find_element(By.ID, self.permanent_address_locator)
            permanent_address_filed.send_keys("Дворцовый мост, вид на Эрмитаж")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_area_locator)

            assert "Дворцовый мост, вид на Эрмитаж" in result_box.text
            print("Тест 04 успешно пройден!")
        finally:
            self.tear_down_test()

    def test_case_05(self): #Тест05 email не без домена
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()

            email_field = self.get_driver().find_element(By.ID, self.email_locator)
            email_field.send_keys("python_avtomat@")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            email_filed = self.get_driver().find_element(By.CSS_SELECTOR, "input[type='email']")
            validation_message = self.get_driver().execute_script("return arguments[0].validationMessage", email_filed)
            #result_box = driver.find_element(By.ID, result_area_locator)

            assert 'Введите часть адреса после символа "@"' in validation_message
            print("Тест 05 успешно пройден!")
        finally:
            self.tear_down_test()

    def test_case_06(self): #Тест06 пустые поля
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()

            full_name_field = self.get_driver().find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("")

            email_field = self.get_driver().find_element(By.ID, self.email_locator)
            email_field.send_keys("")

            current_address_field = self.get_driver().find_element(By.ID, self.current_address_locator)
            current_address_field.send_keys("")

            permanent_address_filed = self.get_driver().find_element(By.ID, self.permanent_address_locator)
            permanent_address_filed.send_keys("")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_area_locator)

            assert "" in result_box.text
            print("Тест 06 успешно пройден!")
        finally:
            self.tear_down_test()

    def test_case_07(self): # Тест 07 SQL инъекция
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()

            email_filed = self.get_driver().find_element(By.ID , self.email_locator)
            email_filed.send_keys("' OR '1'='1")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            email_filed = self.get_driver().find_element(By. CSS_SELECTOR, "input[type='email']")
            validation_message = self.get_driver().execute_script("return arguments[0].validationMessage", email_filed)
            assert 'Адрес электронной почты должен содержать символ "@"' in validation_message
            print("Тест 07 успешно пройден!")
        finally:
            self.tear_down_test()

    def test_case_08(self): # Тест 08 максимальная длина поля имени
        print("Рефакторинг - итерация 2")
        try:
            self.set_up_test()

            full_name_filed = self.get_driver().find_element(By.ID, self.full_name_locator)
            full_name_filed.send_keys("ПримерТекстаДляПроверкиВалидацииПоляВводаИмениКоторыйСпециальноСозданЧтобыПревыситьЛимитРовноНаОдинСимвол1")

            submit_button = self.get_driver().find_element(By.ID, self.button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_area_locator)
            assert "1" in result_box.text
            print("Тест 08 провален! Поле принимает более 100 символов!")

        finally:
            self.tear_down_test()

test_suite = TestSuite(TestSuite.url, TestSuite.driver)
test_suite.test_case_01()
test_suite.test_case_02()
test_suite.test_case_03()
test_suite.test_case_04()
test_suite.test_case_05()
test_suite.test_case_06()
test_suite.test_case_07()
test_suite.test_case_08()