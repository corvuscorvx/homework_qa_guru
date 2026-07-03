import os
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.text_box_page import TextBoxPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def text_box_page(driver):
    return TextBoxPage(driver)


@pytest.fixture(scope="function")
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture(scope="function")
def temp_test_file():
    file_name = "test_image.jpg"
    temp_file_path = os.path.abspath(file_name)
    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write("fake image data")

    yield temp_file_path

    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
