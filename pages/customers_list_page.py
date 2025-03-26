from locators.customers_list_locators import CustomersListLocators as loc
from pages.base_page import BasePage


class CustomersListPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def sort_by_name(self):
        return self.find_element(loc.SORTING_BY_NAME_BTN)

    def sort_btn_click(self):
        self.sort_by_name().click()