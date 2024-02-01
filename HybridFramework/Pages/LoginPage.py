from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):

    #Locators

    email_address_field_name = (By.NAME, "email")
    password_field_id = (By.NAME, "password")
    login_button_xpath = (By.XPATH, "//input[@type='submit']")
    warning_message_xpath = (By.XPATH, "//div[@id='account-login']/div[1]")


    def __init__(self, driver):
        super().__init__(driver)

    #Methods

    def enter_email(self, email_address_text):
        self.type_into_element(email_address_text, self.email_address_field_name)

    def enter_password(self, password_text):
        self.type_into_element(password_text, self.password_field_id)

    def click_on_login_button(self):
        self.do_click(self.login_button_xpath)

    def login_into_application(self, email_address_text, password_text):
        self.enter_email(email_address_text)
        self.enter_password(password_text)
        self.click_on_login_button()

    def retrieve_warning_message(self):
        return self.retrieve_element_text(self.warning_message_xpath)
