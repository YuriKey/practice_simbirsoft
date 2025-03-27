from data.urls import Urls
from pages.add_customer_page import AddCustomerPage
from utils import name_code_generator as ng, table_parser as tp
import allure
import pytest

urls = Urls()


@allure.story("Add Customer")
@allure.testcase("AT00_Add new customer")
@allure.description("Test verifies that add customer page is opened correctly")
@pytest.mark.parametrize(
    "url, expected_title",
    [
        (urls.MANAGER_URL, "XYZ Bank"),
        (urls.ADD_CUSTOMER, "XYZ Bank"),
    ],
)
def test_page_open(browser, url, expected_title):
    page = AddCustomerPage(browser)
    with allure.step(f"Open page {url}"):
        page.open(url)

    with allure.step(f"Check current URL: {url}"):
        assert page.browser.current_url == url, f"Site isn't open: {url}"
    with allure.step(f"Check title: {expected_title}"):
        assert page.browser.title == expected_title, f"Wrong title: {page.browser.title}"


@allure.story("Add Customer")
@allure.testcase("AT00_Add new customer")
@allure.description("Test verifies that the page contains all the necessary fields.")
@pytest.mark.parametrize(
    "field_locator, expected_placeholder, field_name",
    [
        ("first_name_field", "First Name", "First name"),
        ("last_name_field", "Last Name", "Last name"),
        ("post_code_field", "Post Code", "Post code"),
    ],
)
def test_fields(browser, field_locator, expected_placeholder, field_name):
    page = AddCustomerPage(browser)
    with allure.step(f"Open add customer page"):
        page.open(urls.ADD_CUSTOMER)
    add_btn = page.submit_button()

    field_element = getattr(page, field_locator)()
    placeholder = field_element.get_attribute("placeholder")

    with allure.step(f"Check button visibility and text"):
        assert add_btn.is_displayed(), "Submit button not found."
        assert add_btn.text == "Add Customer", "Submit button text is incorrect."
    with allure.step(f"Check field visibility and placeholder"):
        assert field_element.is_displayed(), f"{field_name} field not found."
        assert placeholder == expected_placeholder, f"Wrong {field_name} placeholder: '{placeholder}'"


@allure.story("Add Customer")
@allure.testcase("AT00_Add new customer")
@allure.description("Test verifies that the customer is added successfully.")
def test_add_customer(browser):
    page = AddCustomerPage(browser)
    with allure.step(f"Open add customer page"):
        page.open(urls.ADD_CUSTOMER)

    post_code = ng.post_code_generator()
    first_name = ng.first_name_generator(post_code)
    last_name = ng.last_name_generator()

    with allure.step(f"Fill out fields"):
        page.post_code_field().send_keys(post_code)
        page.first_name_field().send_keys(first_name)
        page.last_name_field().send_keys(last_name)

    with allure.step(f"Submit button click"):
        page.submit_button().click()

    alert = browser.switch_to.alert
    actual_alert_text = alert.text
    with allure.step(f"Check alert message"):
        assert 'Customer added successfully with customer id' in actual_alert_text, 'Alert message is incorrect'
    alert.accept()

    with allure.step(f"Follow to customers list"):
        page.customers_list_btn().click()
    customer_data = tp.get_name_row(browser, first_name)

    with allure.step(f"Check customer data"):
        assert customer_data['first name'] == first_name, 'Customer first name not found'
        assert customer_data['last name'] == last_name, 'Customer last name not found'
        assert customer_data['post code'] == post_code, 'Customer post code not found'
