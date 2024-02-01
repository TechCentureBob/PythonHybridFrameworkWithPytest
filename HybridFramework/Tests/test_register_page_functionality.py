import time

from Pages.AccountSuccessPage import AccountSuccessPage
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage
from Tests.BaseTest import BaseTest


class TestRegisterPage(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_register_page()
        register_page = RegisterPage(self.driver)
        register_page.register_an_account("Kevin", "Lee", self.generate_email_with_time_stamp(),
                                          "1234567890", "1234567", "1234567", "no", "select")
        account_success_page = AccountSuccessPage(self.driver)
        actual_message = account_success_page.retrieve_account_creation_message()
        assert actual_message == "Your Account Has Been Created!"

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_register_page()
        register_page = RegisterPage(self.driver)
        register_page.register_an_account("Kevin", "Lee", self.generate_email_with_time_stamp(),
                                          "1234567890", "1234567", "1234567", "yes", "select")
        account_success_page = AccountSuccessPage(self.driver)
        actual_message = account_success_page.retrieve_account_creation_message()
        assert actual_message == "Your Account Has Been Created!"

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_register_page()
        register_page = RegisterPage(self.driver)
        register_page.register_an_account("Kevin", "Lee", "amotooricap9@gmail.com",
                                          "1234567890", "1234567", "1234567", "yes", "select")

        expected_message = "Warning: E-Mail Address is already registered!"
        actual_message = register_page.retrieve_duplicate_email_warning()
        assert actual_message == expected_message

    def test_register_without_filling_out_fields(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_register_page()
        register_page = RegisterPage(self.driver)
        register_page.register_an_account("", "", "",
                                          "", "", "", "", "")

        register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                          "First Name must be between 1 and 32 characters!",
                                          "Last Name must be between 1 and 32 characters!",
                                          "E-Mail Address does not appear to be valid!",
                                          "Telephone must be between 3 and 32 characters!",
                                          "Password must be between 4 and 20 characters")










