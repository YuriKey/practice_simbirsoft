from data.urls import Urls
from pages.customers_list_page import CustomersListPage
from utils import table_parser as tp
import pytest

urls = Urls()


def test_page_open(browser):
    page = CustomersListPage(browser)
    page.open(urls.CUSTOMERS_LIST)
    assert page.browser.current_url == urls.CUSTOMERS_LIST, 'Site isn`t open'
    assert page.browser.title == "XYZ Bank", 'Wrong title'


@pytest.mark.parametrize(
    "sort_order, expected_sorting",
    [
        ("asc", False),
        ("desc", True),
    ],
)
def test_sort_customer_list(browser, sort_order, expected_sorting):
    page = CustomersListPage(browser)
    page.open(urls.CUSTOMERS_LIST)

    origin_list = tp.get_name_list(browser)

    if sort_order == "asc":
        page.sort_btn_click()
        page.sort_btn_click()
    elif sort_order == "desc":
        page.sort_btn_click()

    actual_list = tp.get_name_list(browser)
    expected_list = sorted(origin_list, reverse=expected_sorting)

    assert actual_list == expected_list, f'List is not sorted by {sort_order}'
