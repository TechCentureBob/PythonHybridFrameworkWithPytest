from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    # Locators
    search_box_field = (By.NAME, "search")
    search_button_xpath = (By.XPATH, "//button[@class='btn btn-default btn-lg']")
    my_account_drop_menu = (By.XPATH, "//span[text()= 'My Account']")
    login_option_link_text = (By.LINK_TEXT, "Login")
    register_option_link_text = (By.LINK_TEXT, "Register")

    # Constructor

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.url)

    # Home Page Methods

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name,self.search_box_field)

    def click_on_search_button(self):
        self.do_click(self.search_button_xpath)

    def click_on_my_account_drop_menu(self):
        self.do_click(self.my_account_drop_menu)

    def click_login_option(self):
        self.do_click(self.login_option_link_text)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        self.click_login_option()

    def search_for_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def select_register_option(self):
        self.do_click(self.register_option_link_text)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        self.select_register_option()

    # Python Hybrid Framework with Pytest






