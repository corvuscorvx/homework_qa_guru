from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_element(self, locator):  # locator = (By.XPATH, locator)
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element.text

    def get_element_attribute(self, locator, attribute_name="value"):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element.get_attribute(attribute_name)

    def tear_down_test(self):
        self.driver.quit()
