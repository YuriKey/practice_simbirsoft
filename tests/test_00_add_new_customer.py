from utils import name_code_generator as ng
from data.urls import Urls
from pages.add_customer_page import AddCustomerPage
import pytest

urls = Urls()


@pytest.mark.parametrize(
    "url, expected_title",
    [
        (urls.MANAGER_URL, "XYZ Bank"),
        (urls.ADD_CUSTOMER, "XYZ Bank"),
    ],
)
def test_page_open(browser, url, expected_title):
    page = AddCustomerPage(browser)
    page.open(url)

    assert page.browser.current_url == url, f"Site isn't open: {url}"
    assert page.browser.title == expected_title, f"Wrong title: {page.browser.title}"


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
    page.open(urls.ADD_CUSTOMER)

    field_element = getattr(page, field_locator)()
    placeholder = field_element.get_attribute("placeholder")

    assert field_element.is_displayed(), f"{field_name} field not found."
    assert placeholder == expected_placeholder, f"Wrong {field_name} placeholder: '{placeholder}'"


def test_form_fill(browser):
    page = AddCustomerPage(browser)
    page.open(urls.ADD_CUSTOMER)

    post_code = ng.post_code_generator()
    first_name = ng.first_name_generator(post_code)
    last_name = ng.last_name_generator()

    page.post_code_field().send_keys(post_code)
    page.first_name_field().send_keys(first_name)
    page.last_name_field().send_keys(last_name)

    page.submit_button().click()

    alert = browser.switch_to.alert
    actual_alert_text = alert.text
    assert actual_alert_text == 'Customer added successfully with customer id :6', 'Alert message is incorrect'

