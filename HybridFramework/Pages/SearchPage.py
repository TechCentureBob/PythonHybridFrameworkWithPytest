from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchPage(BasePage):

    #   Locators:
    valid_hp_product_link_text = (By.LINK_TEXT, "HP LP3065")
    no_product_message_xpath = (By.XPATH, "//input[@id='button-search']/following-sibling::p")

    # Constructor

    def __init__(self, driver):
        super().__init__(driver)

    #Methods

    def display_status_of_valid_product(self):
        return self.check_display_status_of_element(self.valid_hp_product_link_text)

    def retrieve_no_product_message(self):
        return self.retrieve_element_text(self.no_product_message_xpath)