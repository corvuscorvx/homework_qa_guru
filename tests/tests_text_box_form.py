# TODO: сдлеать чтобы строка с open_url не повторялась в тестах
def test_positive_data(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_full_name("Avtomat Avtomatov")
    text_box_page.click_submit_button()
    actual_name = text_box_page.get_actual_data()
    assert "Avtomat Avtomatov" in actual_name


def test_positive_mail(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_email("Avtomat@mail.com")
    text_box_page.click_submit_button()
    actual_email = text_box_page.get_actual_data()
    assert "Avtomat@mail.com" in actual_email


def test_positive_current_address(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_current_address("Eto vremenniy address, dom 1, kv 2, ulica 3")
    text_box_page.click_submit_button()
    actual_current_address = text_box_page.get_actual_data()
    assert "Eto vremenniy address, dom 1, kv 2, ulica 3" in actual_current_address


def test_positive_permanent_address(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_permanent_address("A eto address propiski, tut tolko gorod dorog")
    text_box_page.click_submit_button()
    actual_permanent_address = text_box_page.get_actual_data()
    assert "A eto address propiski, tut tolko gorod dorog" in actual_permanent_address


def test_email_without_username(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_email("@mail.com")
    text_box_page.click_submit_button()
    email_failed = text_box_page.get_email_validation_message()
    assert 'Введите часть адреса до символа "@"' in email_failed


def test_email_without_at(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_email("Avtomatmail.com")
    text_box_page.click_submit_button()
    email_failed = text_box_page.get_email_validation_message()
    assert 'Адрес электронной почты должен содержать символ "@"' in email_failed


def test_email_without_domain(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_email("Avtomat@")
    text_box_page.click_submit_button()
    email_failed = text_box_page.get_email_validation_message()
    assert 'Введите часть адреса после символа "@"' in email_failed


def test_email_with_a_space(text_box_page):
    text_box_page.open_url("https://qa-guru.github.io/one-page-form/text-box.html")
    text_box_page.input_email("Avto mat@mail.com")
    text_box_page.click_submit_button()
    email_failed = text_box_page.get_email_validation_message()
    assert 'Часть адреса до символа "@" не должна содержать символ " "' in email_failed
