import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    LOGIN_FILED_LOCATOR = (By.ID, "login-input")
    PASSWORD_FILED_LOCATOR = (By.ID, "password-input")
    LOGIN_BUTTON_LOCATOR = (By.ID, "submit-button")
    ERROR_MESSAGE_LOCATOR = (By.ID, "error-message")


    def __init__(self, browser_name, url): #Рефакторинг 1 - изменение метода инициализации
        self.browser_name = browser_name.lower()
        self.url = url
        self.driver = None

    # def __init__(self, driver, url):
    #     self.driver = driver
    #     self.url = url

    def set_up_test(self):  #Рефакторинг 01 - изменение метода на роботу с разными браузерами
        if self.browser_name == "chrome":
            self.driver = webdriver.Chrome()
        elif self.browser_name == "firefox":
            self.driver = webdriver.Firefox()
        elif self.browser_name == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError(
                f"\"self.browser_name\" может быть \"chrome\", \"firefox\" или \"edge\". У вас: {self.browser_name}")
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

    #def set_up_test(self):
    #   self.driver = webdriver.Chrome()
    #   self.driver.get(self.url)
    #   self.driver.maximize_window()
    #   time.sleep(3)

    def tear_down_test(self):
        if self.driver:
            self.driver.quit()

    def test_case_01(self): #Тест 01 пустые поля
        try:
            self.set_up_test()

            login_filed = self.driver.find_element(*self.LOGIN_FILED_LOCATOR)
            login_filed.send_keys("")

            password_filed = self.driver.find_element(*self.PASSWORD_FILED_LOCATOR)
            password_filed.send_keys("")

            login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
            login_button.click()

            time.sleep(3)

            error_message = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)
            assert "Login and password are required (minimum 3 and 6 characters)" in error_message.text
            print("Тест 01 пройден успешно!")
        finally:
            self.tear_down_test()

    def test_case_02(self): #Поле логин < 3 символов
        try:
            self.set_up_test()

            login_filed = self.driver.find_element(*self.LOGIN_FILED_LOCATOR)
            login_filed.send_keys("12")

            login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
            login_button.click()

            time.sleep(3)

            error_message = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)
            assert "Login must be at least 3 characters" in error_message.text
            print("Тест 02 пройден успешно!")
        finally:
            self.tear_down_test()

    def test_case_03(self): #Поле пароль < 6 символов
        try:
            self.set_up_test()

            login_filed = self.driver.find_element(*self.LOGIN_FILED_LOCATOR)
            login_filed.send_keys("123")

            password_filed = self.driver.find_element(*self.PASSWORD_FILED_LOCATOR)
            password_filed.send_keys("12345")

            login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
            login_button.click()

            time.sleep(3)

            error_message = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)
            assert "Password must be at least 6 characters" in error_message.text
            print("Тест 03 пройден успешно!")
        finally:
            self.tear_down_test()

    def test_case_04(self): #пустое поле логин
        try:
            self.set_up_test()

            password_filed = self.driver.find_element(*self.PASSWORD_FILED_LOCATOR)
            password_filed.send_keys("1")

            login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
            login_button.click()

            time.sleep(3)

            error_message = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)
            assert "Login is required (minimum 3 characters)" in error_message.text
            print("Тест 04 пройден успешно!")
        finally:
            self.tear_down_test()

    def test_case_05(self): #поле пароль пустое
        try:
            self.set_up_test()

            login_filed = self.driver.find_element(*self.LOGIN_FILED_LOCATOR)
            login_filed.send_keys("123")

            login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
            login_button.click()

            time.sleep(3)

            error_message = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)
            assert "Password is required (minimum 6 characters)" in error_message.text
            print("Тест 05 пройден успешно!")
        finally:
            self.tear_down_test()

    def test_case_06(self): #неверные данные
        try:
            self.set_up_test()

            login_filed = self.driver.find_element(*self.LOGIN_FILED_LOCATOR)
            login_filed.send_keys("123")

            password_filed = self.driver.find_element(*self.PASSWORD_FILED_LOCATOR)
            password_filed.send_keys("123456")

            login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
            login_button.click()

            time.sleep(3)

            error_message = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)
            assert "Wrong login or password" in error_message.text
            print("Тест 06 пройден успешно!")
        finally:
            self.tear_down_test()


url = "https://qa-guru.github.io/one-page-form/login.html"
browser_name = "chrome"
login_page = LoginPage(browser_name, url)
login_page.test_case_01()
login_page.test_case_02()
login_page.test_case_03()
login_page.test_case_04()
login_page.test_case_05()
login_page.test_case_06()
