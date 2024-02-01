from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Methods
    def type_into_element(self, text, locator):
        element = self.get_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def do_click(self,locator):
        element = self.get_element(locator)
        element.click()

    def check_display_status_of_element(self, locator):
        element = self.get_element(locator)
        return element.is_displayed()

    def retrieve_element_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def get_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element
