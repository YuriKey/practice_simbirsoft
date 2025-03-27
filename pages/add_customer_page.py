from locators.add_customer_locators import AddCustomerLocators as loc
from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def post_code_field(self):
        return self.find_element(loc.POST_CODE_FIELD)

    def first_name_field(self):
        return self.find_element(loc.FIRST_NAME_FIELD)

    def last_name_field(self):
        return self.find_element(loc.LAST_NAME_FIELD)

    def submit_button(self):
        return self.find_element(loc.ADD_BUTTON)

    def customers_list_btn(self):
        return self.find_element(loc.CUSTOMERS_LIST_BUTTON)
