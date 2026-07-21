import pytest


@pytest.mark.parametrize("login, password, error_message", [
    ("login1", "password2", "Wrong login or password"),
    ("", "password", "Login is required (minimum 3 characters)"),
    ("login", "", "Password is required (minimum 6 characters)"),
    ("12", "123456", "Login must be at least 3 characters"),
    ("123", "12345", "Password must be at least 6 characters"),
    ("", "", "Login and password are required (minimum 3 and 6 characters)")
])
def test_negative_login(login_page_factory, login, password, error_message):
    login_page_factory.input_login(login)
    login_page_factory.input_password(password)
    login_page_factory.click_login_button()

    assert login_page_factory.get_error_message(error_message) is True
