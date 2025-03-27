from ui_tests.data.urls import Urls
from ui_tests.pages.customers_list_page import CustomersListPage
from ui_tests.utils import table_parser as tp
import allure
import pytest

urls = Urls()


@allure.story("Sort Customer List")
@allure.testcase("AT01_Add new customer")
@allure.description("Customer list page open")
def test_page_open(browser):
    page = CustomersListPage(browser)
    with allure.step('Open Customer list page'):
        page.open(urls.CUSTOMERS_LIST)
    with allure.step('Verify Customer list page'):
        assert page.browser.current_url == urls.CUSTOMERS_LIST, 'Site isn`t open'
        assert page.browser.title == "XYZ Bank", 'Wrong title'


@allure.story("Sort Customer List")
@allure.testcase("AT01_Add new customer")
@allure.description("Customer list page sorting")
@pytest.mark.parametrize(
    "sort_order, expected_sorting",
    [
        ("ascending", False),
        ("descending", True),
    ],
)
def test_sort_customer_list(browser, sort_order, expected_sorting):
    page = CustomersListPage(browser)
    with allure.step('Open Customer list page'):
        page.open(urls.CUSTOMERS_LIST)

    origin_list = tp.get_name_list(browser)

    if sort_order == "ascending":
        with allure.step('Sorting Customer list by First Name ascending'):
            page.sort_btn_click()
            page.sort_btn_click()
    elif sort_order == "descending":
        with allure.step('Sorting Customer list by First Name descending'):
            page.sort_btn_click()

    actual_list = tp.get_name_list(browser)
    expected_list = sorted(origin_list, reverse=expected_sorting)

    with allure.step(f'Verify Customer list is sorted by {sort_order}'):
        assert actual_list == expected_list, f'List is not sorted by {sort_order}'
