from utils import table_parser as tp, find_avg_name_length as fnl
from data.urls import Urls
from pages.customers_list_page import CustomersListPage
import allure

urls = Urls()


@allure.story("Delete a customer")
@allure.testcase("AT02_Delete a customer")
@allure.description("Verify that after deleting a customer, the customer is no longer displayed in the table")
def test_avg_name_delete(browser):
    page = CustomersListPage(browser)
    with allure.step("Open the customers list page"):
        page.open(urls.CUSTOMERS_LIST)

    origin_list = tp.get_name_list(browser)
    name = fnl.find_name_closest_to_average(origin_list)

    delete_btn_loc = ("xpath", f"//tr[td[@class='ng-binding' and text()='{name}']]//button[@ng-click='deleteCust(cust)']")
    with allure.step("Check delete button for customer`s row"):
        assert page.element_is_visible(delete_btn_loc)
        assert page.find_element(delete_btn_loc).text == "Delete"

    with allure.step("Delete customer"):
        page.click(delete_btn_loc)
    updated_list = tp.get_name_list(browser)

    with allure.step("Verify that the customer is not displayed in the table"):
        assert name not in updated_list
