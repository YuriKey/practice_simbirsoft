import allure
import pytest

from ui_tests.data.urls import Urls
from ui_tests.pages.add_customer_page import AddCustomerPage
from ui_tests.utils import name_code_generator as ng, table_parser as tp

urls = Urls()


@allure.epic("Тестирование UI.")
@allure.feature("Управление клиентами.")
@allure.story("Добавление нового клиента.")
@allure.testcase("AT00_Добавление нового клиента.")
@allure.title("Добавление нового клиента.")
class TestAddNewCustomer:
    @allure.title("Проверка открытия страницы.")
    @allure.description("""
    Тест проверяет:
    1. Открытие переданной в параметр страницы.
    2. Идентичность текущего и ожидаемого URL.
    3. Идентичность полученного и ожидаемого заголовков страницы.
    """)
    @pytest.mark.parametrize(
        "url, expected_title",
        [
            (urls.MANAGER_URL, "XYZ Bank"),
            (urls.ADD_CUSTOMER, "XYZ Bank"),
        ],
    )
    def test_page_open(self, browser, url, expected_title):
        page = AddCustomerPage(browser)
        with allure.step(f"Открыть страницу {url} ."):
            page.open(url)

        with allure.step(f"Проверить текущий URL: {url} ."):
            assert page.browser.current_url == url, f"Site isn't open: {url}"
        with allure.step(f"Проверить заголовок страницы: {expected_title} ."):
            assert page.browser.title == expected_title, f"Wrong title: {page.browser.title}"

    @allure.title("Проверка наличия полей и кнопки 'Add Customer' на странице.")
    @allure.description("""
    Тест проверяет:
    1. Открытие страницы добавления клиента.
    2. Наличие кнопки добавления на странице и корректность ее текста.
    3. Наличие полей формы и корректность их плейсхолдеров.
    """)
    @pytest.mark.parametrize(
        "field_locator, expected_placeholder, field_name",
        [
            ("first_name_field", "First Name", "First name"),
            ("last_name_field", "Last Name", "Last name"),
            ("post_code_field", "Post Code", "Post code"),
        ],
    )
    def test_fields(self, browser, field_locator, expected_placeholder, field_name):
        page = AddCustomerPage(browser)
        with allure.step("Открыть страницу добавления клиента."):
            page.open(urls.ADD_CUSTOMER)
        add_btn = page.submit_button()

        field_element = getattr(page, field_locator)()
        placeholder = field_element.get_attribute("placeholder")

        with allure.step("Проверить наличие кнопки добавления на странице и ее текст."):
            assert add_btn.is_displayed(), "Submit button not found."
            assert add_btn.text == "Add Customer", "Submit button text is incorrect."
        with allure.step(f"Проверить наличие поля {field_name} и его плейсхолдера."):
            assert field_element.is_displayed(), f"{field_name} field not found."
            assert placeholder == expected_placeholder, f"Wrong {field_name} placeholder: '{placeholder}'"

    @allure.title("Проверка успешного добавления клиента.")
    @allure.description("""
    Тест проверяет:
    1. Открытие страницы добавления клиента.
    2. Заполнение полей формы.
    3. Нажатие кнопки добавления клиента.
    4. Наличие и корректность текста уведомления об успешном добавлении клиента.
    5. Наличие добавленного клиента в таблице.""")
    def test_add_customer(self, browser):
        page = AddCustomerPage(browser)
        with allure.step("Открыть страницу добавления клиента"):
            page.open(urls.ADD_CUSTOMER)

        post_code = ng.post_code_generator()
        first_name = ng.first_name_generator(post_code)
        last_name = ng.last_name_generator()

        with allure.step("Заполнить поля формы клиента."):
            page.post_code_field().send_keys(post_code)
            page.first_name_field().send_keys(first_name)
            page.last_name_field().send_keys(last_name)

        with allure.step("Нажать кнопку добавления клиента."):
            page.submit_button().click()

        alert = browser.switch_to.alert
        actual_alert_text = alert.text
        with allure.step("Проверить наличие и текст уведомления об успешном добавлении клиента."):
            assert "Customer added successfully with customer id" in actual_alert_text, "Alert message is incorrect"
        alert.accept()

        with allure.step("Открыть список клиентов."):
            page.customers_list_btn().click()
        customer_data = tp.get_name_row(browser, first_name)

        with allure.step("Проверить наличие добавленного клиента в таблице."):
            assert customer_data["first name"] == first_name, "Customer first name not found"
            assert customer_data["last name"] == last_name, "Customer last name not found"
            assert customer_data["post code"] == post_code, "Customer post code not found"
