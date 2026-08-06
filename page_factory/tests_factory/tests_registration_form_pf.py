import pytest


@pytest.mark.parametrize("first_name, last_name, gender, number", [
    ("Polnoe", "Imya", "Male", "1234567890"),
    ("Я", "Ю", "Other", "1111111111"),
    ("A" * 250, "B" * 250, "Female", "0" * 10)
])
def test_positive_required_fields(registration_page_factory, first_name, last_name, gender, number):
    registration_page_factory.close_banner()
    registration_page_factory.input_first_name(first_name)
    registration_page_factory.input_last_name(last_name)
    registration_page_factory.select_gender(gender)
    registration_page_factory.input_number(number)
    registration_page_factory.scroll_to_footer()
    registration_page_factory.click_submit_button()

    output = registration_page_factory.get_result_form()

    assert output is not None, "Блок с результатами не отобразился"
    assert first_name.strip() in output, f"Имя {first_name} не найдено в форме результатов"
    assert last_name.strip() in output, f"Фамилия {last_name} не найдена в форме результатов"
    assert gender.strip() in output, f"Пол {gender} не найден в форме результатов"
    assert number.strip() in output, f"Номер {number} не найден в форме результатов"


@pytest.mark.parametrize(
    "first_name, last_name, email, gender, number, date_tuple, subjects, hobbies, current_address, state, city", [
        ("Polnoe", "Imya", "pochta@guru.qa", "Male", "1234567890", (1, 12, 1999), ["Maths", "Physics", "Chemistry"],
         ["Sports", "Reading"], "Временный адрес", "Uttar Pradesh", "Lucknow"),
        ("A", "B", "pochta@guru.ru", "Female", "0" * 10, (31, 1, 1900), ["Civics"], ["Sports"], "A" * 256, "Rajasthan",
         "Jaiselmer")
    ])
def test_positive_all_fields(registration_page_factory, temp_test_file, first_name, last_name, email, gender, number,
                             date_tuple, subjects, hobbies, current_address, state, city):
    registration_page_factory.close_banner()
    registration_page_factory.input_first_name(first_name)
    registration_page_factory.input_last_name(last_name)
    registration_page_factory.input_email(email)
    registration_page_factory.select_gender(gender)
    registration_page_factory.input_number(number)
    day, month, year = date_tuple
    registration_page_factory.select_date_of_birth(day, month, year)
    registration_page_factory.input_subjects(subjects)
    registration_page_factory.select_hobbies(hobbies)
    registration_page_factory.scroll_to_footer()
    file_path, file_name = temp_test_file
    registration_page_factory.upload_file(file_path)
    registration_page_factory.input_current_address(current_address)
    registration_page_factory.select_state(state)
    registration_page_factory.select_city(city)
    registration_page_factory.click_submit_button()

    output = registration_page_factory.get_result_form()
    expected_date = registration_page_factory.get_expected_birth_date_text(day, month, year)

    assert output is not None, "Блок с результатами не отобразился"
    assert first_name.strip() in output, f"Имя {first_name} не найдено в форме результатов"
    assert last_name.strip() in output, f"Фамилия {last_name} не найдена в форме результатов"
    assert email.strip() in output, f"Почта {email} не найдена в форме результатов"
    assert gender.strip() in output, f"Пол {gender} не найден в форме результатов"
    assert number.strip() in output, f"Номер {number} не найден в форме результатов"
    assert expected_date in output, f"Дата рождения '{expected_date}' не найдена в форме результатов"
    for subject in subjects:
        assert subject in output, f"Предмет {subject} отсутствует в форме результатов"
    for hobby in hobbies:
        assert hobby in output, f"Хобби {hobby} отсутствует в форме результатов"
    assert file_name in output, f"Файл {file_name} не найден в форме результатов"
    assert current_address.strip() in output, f"Адрес {current_address} не найден в форме результатов"
    assert state.strip() in output, f"Штат {state} не найден в форме результатов"
    assert city.strip() in output, f"Город {city} не найден в форме результатов"


@pytest.mark.parametrize("first_name, last_name, gender, number, error_text", [
    ("", "Imya", "Male", "1234567890", "Please fill required fields and enter a valid 10-digit mobile number."),
    ("Polnoe", "", "Other", "1111111111", "Please fill required fields and enter a valid 10-digit mobile number."),
    ("Polnoe", "Imya", "", "0987654321", "Please fill required fields and enter a valid 10-digit mobile number."),
    ("Polnoe", "Imya", "Female", "", "Please fill required fields and enter a valid 10-digit mobile number.")
])
def test_negative_required_fields(registration_page_factory, first_name, last_name, gender, number, error_text):
    registration_page_factory.close_banner()
    registration_page_factory.input_first_name(first_name)
    registration_page_factory.input_last_name(last_name)
    registration_page_factory.select_gender(gender)
    registration_page_factory.input_number(number)
    registration_page_factory.scroll_to_footer()
    registration_page_factory.click_submit_button()
    actual_error = registration_page_factory.get_error_message()

    assert error_text in actual_error
