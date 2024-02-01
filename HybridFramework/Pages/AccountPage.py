from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AccountPage(BasePage):

    #Locators:

    edit_your_account_information_option_link_text = (By.LINK_TEXT, "Edit your account information")

    #Method

    def display_status_of_edit_your_information_option(self):
        return self.check_display_status_of_element(self.edit_your_account_information_option_link_text)
