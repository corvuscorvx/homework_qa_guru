import pytest
import allure

@allure.epic("Веб-форма")
@allure.feature("Отправка формы")
@allure.story("Успешная отправка заполненных полей")
@allure.title("Позитивный сценарий")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("full_name, email, current_address, permanent_address", [
    ("Polnoe Imya", "Pochta@mail.ru", "Ulica, dom 8, kV.99", "Apteca, ulica, fonar"),
    ("Ю Я", "a@b.ru", "1", "2")
])
def test_positive_data(text_box_page_factory, full_name, email, current_address, permanent_address):
    text_box_page_factory.input_full_name(full_name)
    text_box_page_factory.input_email(email)
    text_box_page_factory.input_current_address(current_address)
    text_box_page_factory.input_permanent_address(permanent_address)
    text_box_page_factory.click_submit_button()

    output = text_box_page_factory.get_output_data()

    assert output is not None, "Блок с результатами не отобразился"
    assert output["full_name"] == full_name.strip()
    assert output["email"] == email.strip()
    assert output["current_address"] == current_address.strip()
    assert output["permanent_address"] == permanent_address.strip()

@allure.epic("Веб-форма")
@allure.feature("Отправка формы")
@allure.story("Успешная отправка частично заполненных полей")
@allure.title("Позитивный сценарий")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("full_name, email, current_address, permanent_address", [
    ("Poln Im", "", "", ""),
    ("", "milo@qa.guru", "", ""),
    ("", "", "cur adr", ""),
    ("", "", "", "perm adr")
])
def test_positive_partial_data(text_box_page_factory, full_name, email, current_address, permanent_address):
    text_box_page_factory.input_full_name(full_name)
    text_box_page_factory.input_email(email)
    text_box_page_factory.input_current_address(current_address)
    text_box_page_factory.input_permanent_address(permanent_address)
    text_box_page_factory.click_submit_button()

    output = text_box_page_factory.get_output_data()

    assert output is not None, "Форма должна отправляться при частичном заполнении"
    assert output["full_name"] == full_name.strip()
    assert output["email"] == email.strip()
    assert output["current_address"] == current_address.strip()
    assert output["permanent_address"] == permanent_address.strip()

@allure.epic("Веб-форма")
@allure.feature("Отправка формы")
@allure.story("Блокировка некорректного email")
@allure.title("Негативный сценарий")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("invalid_email", [
    "emailnotsobaka",
    "email@@qa.guru",
    "aqa@gu-ru",
    "aq.a@guru",
    "@qa.guru",
    "qa@gu..ru"
])
def test_negative_invalid_email(text_box_page_factory, invalid_email):
    text_box_page_factory.input_email(invalid_email)
    text_box_page_factory.click_submit_button()

    output = text_box_page_factory.get_output_data()
    is_error = text_box_page_factory.is_email_error_present()
    error_message = text_box_page_factory.get_email_validation_message()

    assert output is None, f"Форма отправлена, хотя email '{invalid_email}' невалиден!"
    assert is_error, f"Email'{invalid_email}' не помечен как невалидный!"
    assert error_message != "", "Нет текста ошибки!"
