import datetime
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class Calendar(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()
        self.locators = {
            "month_select": ("CSS", "select[class='react-datepicker__month-select']"),
            "year_select": ("CSS", "select[class='react-datepicker__year-select']")
        }

    def select_date(self, day: int, month: int, year: int):
        self.year_select.click()
        self.driver.find_element(By.CSS_SELECTOR, f"option[value='{year}']").click()

        self.month_select.click()
        self.driver.find_element(By.CSS_SELECTOR, f"option[value='{month - 1}']").click()

        self.driver.find_element(By.CSS_SELECTOR, f"span[data-day='{day}']").click()

    @staticmethod
    def format_to_site_date(day: int, month: int, year: int) -> str:
        date_object = datetime.date(year, month, day)
        month_name = date_object.strftime("%b")
        return f"{day} {month_name} {year}"
