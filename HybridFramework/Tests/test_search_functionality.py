from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage
from Tests.BaseTest import BaseTest


class TestSearch(BaseTest):

    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.search_for_product("HP")
        assert search_page.display_status_of_valid_product(), "The product was not displayed as expected"

    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.search_for_product("Honda")
        actual_text = search_page.retrieve_no_product_message()
        assert actual_text == TestData.expected_no_product_page_message

    def test_search_without_entering_any_product_name(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.search_for_product("")
        actual_text = search_page.retrieve_no_product_message()
        assert actual_text == TestData.expected_no_product_page_message

# Allure Report
# Pytest-html report




