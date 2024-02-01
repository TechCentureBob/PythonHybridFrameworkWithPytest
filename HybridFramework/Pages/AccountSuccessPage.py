from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    # Locator
    account_creation_message_xpath = By.XPATH, "//div[@id='content']/h1"

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    #Methods

    def retrieve_account_creation_message(self):
        return self.retrieve_element_text(self.account_creation_message_xpath)


