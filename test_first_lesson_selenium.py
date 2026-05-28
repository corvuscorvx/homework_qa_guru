import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    #Тест01 постоянный адрес
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)

    permanent_address_filed = driver.find_element(By.ID, "permanentAddress")
    permanent_address_filed.send_keys("Дворцовый мост, вид на Эрмитаж")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)

    result_box = driver.find_element(By.ID, "output")

    assert "Дворцовый мост, вид на Эрмитаж" in result_box.text
    print("Тест 01 успешно пройден!")

    #Тест02 временный адрес
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)

    current_address_field = driver.find_element(By.ID, "currentAddress")
    current_address_field.send_keys("Улица Пушкина, дом Колотушкина")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)

    result_box = driver.find_element(By.ID, "output")

    assert "Улица Пушкина, дом Колотушкина" in result_box.text
    print("Тест 02 успешно пройден!")

    #Тест03 email не по маске
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)

    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("python_avtomat.com")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)

    result_box = driver.find_element(By.ID, "output")

    assert "" in result_box.text
    print("Тест 03 успешно пройден!")

    #Тест04 пустые поля
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)

    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("")

    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("")

    current_address_field = driver.find_element(By.ID, "currentAddress")
    current_address_field.send_keys("")

    permanent_address_filed = driver.find_element(By.ID, "permanentAddress")
    permanent_address_filed.send_keys("")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)

    result_box = driver.find_element(By.ID, "output")

    assert "" in result_box.text
    print("Тест 04 успешно пройден!")

finally:
    driver.quit()

    #неудобства: длинный тест, а не много разных в оддельных файлов, если нужно как-то изменить данные, то возможно придется менять много где. Долго наблюдать за прохождением, сложно исправлять и искать какой-от тест в полотне