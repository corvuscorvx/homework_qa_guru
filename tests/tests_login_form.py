from selenium import webdriver
from pages.login_page import LoginPage


def test_positive_login():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)

    login_page.login("Avtomat@mail.ru", "12345678")

    login_page.tear_down_test()

def test_empty_login():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)

    login_page.login("", "123456")

    error_text = login_page.get_error_message()
    assert "Login is required (minimum 3 characters)" in error_text

    login_page.tear_down_test()

def test_empty_password():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)

    login_page.login("!QAZ2wsx", "")

    error_text = login_page.get_error_message()
    assert "Password is required (minimum 6 characters)" in error_text

    login_page.tear_down_test()

def test_empty_fields():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)

    login_page.login("", "")

    error_text = login_page.get_error_message()
    assert "Login and password are required (minimum 3 and 6 characters)" in error_text

    login_page.tear_down_test()

def test_incorrect_data():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)

    login_page.login("Avtomat@mai", "123456")

    error_text = login_page.get_error_message()
    assert "Wrong login or password" in error_text

    login_page.tear_down_test()

def test_short_password():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)

    login_page.login("Avtomat@mail.ru", "12345")

    error_text = login_page.get_error_message()
    assert "Password must be at least 6 characters" in error_text

    login_page.tear_down_test()

def test_short_login():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)

    login_page.login("Av", "123456")

    error_text = login_page.get_error_message()
    assert "Login must be at least 3 characters" in error_text

    login_page.tear_down_test()
