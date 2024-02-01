import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class RegisterPage(BasePage):
    # Locators:
    first_name_field_id = By.ID, "input-firstname"
    last_name_field_id = By.ID, "input-lastname"
    email_field_id = By.ID, "input-email"
    telephone_field_id = By.ID, "input-telephone"
    password_field_id = By.ID, "input-password"
    confirm_password_field_id = By.ID, "input-confirm"
    agree_field_name = By.NAME, "agree"
    continue_button_xpath = By.XPATH, "//input[@value='Continue']"
    yes_radio_button_xpath = By.XPATH, "//input[@name='newsletter'][@value=1]"
    duplicate_email_warning_xpath = By.XPATH, "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = By.XPATH, "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = By.XPATH, "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = By.XPATH, "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = By.XPATH, "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = By.XPATH, "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = By.XPATH, "//input[@id='input-password']/following-sibling::div"

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Methods

    def enter_first_name(self, first_name_text):
        self.type_into_element(first_name_text, self.first_name_field_id)

    def enter_last_name(self, last_name_text):
        self.type_into_element(last_name_text, self.last_name_field_id)

    def enter_email(self, email_text):
        self.type_into_element(email_text, self.email_field_id)

    def enter_telephone(self, telephone_text):
        self.type_into_element(telephone_text, self.telephone_field_id)

    def enter_password(self, password_text):
        self.type_into_element(password_text, self.password_field_id)

    def enter_password_confirm(self, password_text):
        self.type_into_element(password_text, self.confirm_password_field_id)

    def select_yes_radio_button(self):
        self.do_click(self.yes_radio_button_xpath)

    def select_agree_checkbox_field(self):
        self.do_click(self.agree_field_name)

    def click_on_continue_button(self):
        self.do_click(self.continue_button_xpath)

    def register_an_account(self, first_name_text, last_name_text, email_text,
                            telephone_text, password_text, password_confirm_text,
                            yes_or_no, privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_confirm_text)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning(self):
        return self.retrieve_element_text(self.duplicate_email_warning_xpath)

    def retrieve_policy_warning_message(self):
        return self.retrieve_element_text(self.privacy_policy_warning_xpath)

    def retrieve_warning_message(self, locator):
        return self.retrieve_element_text(locator)

    def verify_all_warnings(self, expected_policy_warning, expected_first_name_warning,
                            expected_last_name_warning, expected_email_warning, expected_phone_warning,
                            expected_password_warning):

        actual_privacy_policy_warning = self.retrieve_policy_warning_message().strip()
        actual_first_name_warning = self.retrieve_warning_message(self.first_name_warning_xpath).strip()
        actual_last_name_warning = self.retrieve_warning_message(self.last_name_warning_xpath).strip()
        actual_email_warning = self.retrieve_warning_message(self.email_warning_xpath).strip()
        actual_phone_warning = self.retrieve_warning_message(self.telephone_warning_xpath).strip()
        actual_password_warning = self.retrieve_warning_message(self.password_warning_xpath).strip()

        assert expected_policy_warning == actual_privacy_policy_warning, "Privacy policy warning does not match"
        assert expected_first_name_warning == actual_first_name_warning, "First name warning does not match"
        assert expected_last_name_warning == actual_last_name_warning, "Last name warning does not match"
        assert expected_email_warning == actual_email_warning, "Email warning does not match"
        assert expected_phone_warning == actual_phone_warning, "Phone warning does not match"
        assert expected_password_warning == actual_password_warning, "Password warning does not match"

        return True

    # Python Hybrid Framework with Pytest
    # Java BDD Hybrid Framework with Cucumber
    # Python Hybrid Framework with Behave








