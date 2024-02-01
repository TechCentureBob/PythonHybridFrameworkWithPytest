from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.AccountPage import AccountPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestLogin(BaseTest):

    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.login_into_application(TestData.valid_login_email, TestData.valid_login_password)
        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_your_information_option()

    def test_login_with_invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.login_into_application(self.generate_email_with_time_stamp(), TestData.valid_login_password)
        actual_message = login_page.retrieve_warning_message()
        assert actual_message == TestData.expected_warning_message_for_login

    def test_login_with_valid_email_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.login_into_application(TestData.valid_login_email, TestData.invalid_login_password)
        actual_message = login_page.retrieve_warning_message()
        assert actual_message == TestData.expected_warning_message_for_login

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.login_into_application("", "")
        actual_message = login_page.retrieve_warning_message()
        assert actual_message == TestData.expected_warning_message_for_login



