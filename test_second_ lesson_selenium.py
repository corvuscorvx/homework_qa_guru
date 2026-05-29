import time
from selenium import webdriver
from selenium.webdriver.common.by import By

full_name_locator = "userName"
email_locator = "userEmail"
current_address_locator = "currentAddress"
permanent_address_locator = "permanentAddress"
button_locator = "submit"
result_area_locator = "output"

def set_up_test(driver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)

def tear_down_test(driver):
    driver.quit()

def test_positive_name(): #Тест 01 полное имя
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        full_name_filed = driver.find_element(By.ID, full_name_locator)
        full_name_filed.send_keys("Автомат Селениумов")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, result_area_locator)
        assert "Автомат Селениумов" in result_box.text
        print("Тест 01 успешно пройден")
    finally:
        tear_down_test(driver)

def test_positive_email(): #Тест 02 email
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        email_filed = driver.find_element(By.ID, email_locator)
        email_filed.send_keys("Pitonist@qaguru.school")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, result_area_locator)
        assert "Pitonist@qaguru.school" in result_box.text
        print("Тест 02 успешно пройден")
    finally:
        tear_down_test(driver)

def test_positive_current_address(): #Тест03 временный адрес
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        current_address_field = driver.find_element(By.ID, current_address_locator)
        current_address_field.send_keys("Улица Пушкина, дом Колотушкина")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, result_area_locator)

        assert "Улица Пушкина, дом Колотушкина" in result_box.text
        print("Тест 03 успешно пройден!")
    finally:
        tear_down_test(driver)

def test_positive_permanent_address(): #Тест04 постоянный адрес
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        permanent_address_filed = driver.find_element(By.ID, permanent_address_locator)
        permanent_address_filed.send_keys("Дворцовый мост, вид на Эрмитаж")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, result_area_locator)

        assert "Дворцовый мост, вид на Эрмитаж" in result_box.text
        print("Тест 04 успешно пройден!")
    finally:
        tear_down_test(driver)

def test_negative_email_not_domain(): #Тест05 email не без домена
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        email_field = driver.find_element(By.ID, email_locator)
        email_field.send_keys("python_avtomat@")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        email_filed = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        validation_message = driver.execute_script("return arguments[0].validationMessage", email_filed)
        #result_box = driver.find_element(By.ID, result_area_locator)

        assert 'Введите часть адреса после символа "@"' in validation_message
        print("Тест 05 успешно пройден!")
    finally:
        tear_down_test(driver)

def test_negative_empty_fields(): #Тест06 пустые поля
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        full_name_field = driver.find_element(By.ID, full_name_locator)
        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, email_locator)
        email_field.send_keys("")

        current_address_field = driver.find_element(By.ID, current_address_locator)
        current_address_field.send_keys("")

        permanent_address_filed = driver.find_element(By.ID, permanent_address_locator)
        permanent_address_filed.send_keys("")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, result_area_locator)

        assert "" in result_box.text
        print("Тест 06 успешно пройден!")
    finally:
        tear_down_test(driver)

def test_negative_sql_email(): # Тест 07 SQL инъекция
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        email_filed = driver.find_element(By.ID , email_locator)
        email_filed.send_keys("' OR '1'='1")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        email_filed = driver.find_element(By. CSS_SELECTOR, "input[type='email']")
        validation_message = driver.execute_script("return arguments[0].validationMessage", email_filed)
        assert 'Адрес электронной почты должен содержать символ "@"' in validation_message
        print("Тест 07 успешно пройден!")
    finally:
        tear_down_test(driver)

def test_negative_full_name_max_limit(): # Тест 08 максимальная длина поля имени
    print("Рефакторинг - итерация 1")
    driver = webdriver.Chrome()
    try:
        set_up_test(driver)

        full_name_filed = driver.find_element(By.ID, full_name_locator)
        full_name_filed.send_keys("ПримерТекстаДляПроверкиВалидацииПоляВводаИмениКоторыйСпециальноСозданЧтобыПревыситьЛимитРовноНаОдинСимвол1")

        submit_button = driver.find_element(By.ID, button_locator)
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, result_area_locator)
        assert "1" in result_box.text
        print("Тест 08 провален! Поле принимает более 100 символов!")

    finally:
        tear_down_test(driver)


test_positive_name()
test_positive_email()
test_positive_current_address()
test_positive_permanent_address()
test_negative_email_not_domain()
test_negative_empty_fields()
test_negative_sql_email()
test_negative_full_name_max_limit()