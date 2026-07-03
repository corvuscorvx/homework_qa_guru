from random import randint
from tests.conftest import temp_test_file


# TODO: сделать, чтобы гендер принимал "male" и тд, а не радио
def test_positive_required_fields(registration_page):
    first_name = "Avtomat"
    last_name = "Avtomatov"
    number = randint(9000000000, 9999999999)
    gender = "gender-radio-1"

    registration_page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    registration_page.close_banner()
    registration_page.input_first_name(first_name)
    registration_page.input_last_name(last_name)
    registration_page.input_mobile_number(number)
    registration_page.select_gender(gender)
    registration_page.scroll_to_footer()
    registration_page.click_submit_button()


# TODO: добавить проверки, чтобы они были не громоздкими и плодили лишние строки (assert) + изменить метод выбора даты
def test_positive_all_fields(registration_page, temp_test_file):
    first_name = "Avtomat"
    last_name = "Avtomatov"
    email = "avtomat@guru.com"
    number = randint(9000000000, 9999999999)
    gender = "gender-radio-1"
    day, month, year = 1, 2, 1990
    expected_subjects = ["Maths", "Physics", "Chemistry"]
    hobbies_list = ["Sports", "Reading"]
    current_address = "Vremenniy address"
    state_value = 4
    city_value = 1

    registration_page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    registration_page.close_banner()
    registration_page.input_first_name(first_name)
    registration_page.input_last_name(last_name)
    registration_page.input_email(email)
    registration_page.input_mobile_number(number)
    registration_page.select_gender(gender)
    registration_page.scroll_to_footer()
    registration_page.select_date_of_birth(day, month, year)
    registration_page.input_subjects(expected_subjects)
    registration_page.select_hobbies(hobbies_list)
    registration_page.upload_picture(temp_test_file)
    registration_page.input_current_address(current_address)
    registration_page.select_state(state_value)
    registration_page.select_city(city_value)
    registration_page.click_submit_button()


def test_negative_empty_first_name(registration_page):
    first_name = ""
    last_name = "Avtomatov"
    number = randint(9000000000, 9999999999)
    gender = "gender-radio-1"
    error_message = "Please fill required fields and enter a valid 10-digit mobile number."

    registration_page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    registration_page.close_banner()
    registration_page.input_first_name(first_name)
    registration_page.input_last_name(last_name)
    registration_page.input_mobile_number(number)
    registration_page.select_gender(gender)
    registration_page.scroll_to_footer()
    registration_page.click_submit_button()
    actual_error = registration_page.get_error_message()

    assert error_message in actual_error


def test_negative_empty_last_name(registration_page):
    first_name = "Ю"
    last_name = ""
    number = randint(9000000000, 9999999999)
    gender = "gender-radio-3"
    error_message = "Please fill required fields and enter a valid 10-digit mobile number."

    registration_page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    registration_page.close_banner()
    registration_page.input_first_name(first_name)
    registration_page.input_last_name(last_name)
    registration_page.input_mobile_number(number)
    registration_page.select_gender(gender)
    registration_page.scroll_to_footer()
    registration_page.click_submit_button()
    actual_error = registration_page.get_error_message()

    assert error_message in actual_error


def test_negative_empty_gender(registration_page):
    first_name = "Ю"
    last_name = "Буква"
    number = randint(9000000000, 9999999999)
    error_message = "Please fill required fields and enter a valid 10-digit mobile number."

    registration_page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    registration_page.close_banner()
    registration_page.input_first_name(first_name)
    registration_page.input_last_name(last_name)
    registration_page.input_mobile_number(number)
    registration_page.scroll_to_footer()
    registration_page.click_submit_button()
    actual_error = registration_page.get_error_message()

    assert error_message in actual_error


def test_negative_empty_number(registration_page):
    first_name = "Ю"
    last_name = "Я"
    gender = "gender-radio-3"
    error_message = "Please fill required fields and enter a valid 10-digit mobile number."

    registration_page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    registration_page.close_banner()
    registration_page.input_first_name(first_name)
    registration_page.input_last_name(last_name)
    registration_page.select_gender(gender)
    registration_page.scroll_to_footer()
    registration_page.click_submit_button()
    actual_error = registration_page.get_error_message()

    assert error_message in actual_error
