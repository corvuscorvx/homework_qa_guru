import os
import pytest
from selenium import webdriver
from page_object.pages.login_page import LoginPage
from page_object.pages.text_box_page import TextBoxPage
from page_object.pages.registration_page import RegistrationPage
from page_factory.pages_factory.login_page_factory import LoginPageFactory


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    driver.get("https://qa-guru.github.io/one-page-form/login.html")
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login_page_factory(driver):
    driver.get("https://qa-guru.github.io/one-page-form/login.html")
    return LoginPageFactory(driver)


@pytest.fixture(scope="function")
def text_box_page(driver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    return TextBoxPage(driver)


@pytest.fixture(scope="function")
def registration_page(driver):
    driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    return RegistrationPage(driver)


@pytest.fixture(scope="function")
def temp_test_file():
    file_name = "test_image.jpg"
    temp_file_path = os.path.abspath(file_name)
    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write("fake image data")

    yield temp_file_path, file_name

    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
