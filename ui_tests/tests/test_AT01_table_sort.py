import allure
import pytest

from ui_tests.data.urls import Urls
from ui_tests.pages.customers_list_page import CustomersListPage
from ui_tests.utils import table_parser as tp

urls = Urls()


@allure.epic("Тестирование UI.")
@allure.feature("Управление клиентами.")
@allure.story("Список клиентов.")
@allure.testcase("AT01_Сортировка списка клиентов.")
@allure.title("Сортировка списка клиентов по имени.")
class TestCustomersListPage:
    @allure.title("Открытие страницы списка клиентов.")
    @allure.description("""
    Тест проверяет:
    1. Открытие страницы со списком клиентов.
    2. Идентичность текущего и ожидаемого URL.
    3. Идентичность текущего и ожидаемого заголовка страницы.
    """)
    def test_page_open(self, browser):
        page = CustomersListPage(browser)
        with allure.step("Открыть страницу со списком клиентов."):
            page.open(urls.CUSTOMERS_LIST)
        with allure.step("Проверить текущий URL и заголовок страницы."):
            assert page.browser.current_url == urls.CUSTOMERS_LIST, "Site isn`t open"
            assert page.browser.title == "XYZ Bank", "Wrong title"

    @allure.title("Сортировка списка клиентов по имени.")
    @allure.description("""
    Тест проверяет:
    1. Открытие страницы со списком клиентов.
    2. Корректность сортировки по имени клиента по возрастанию.
    3. Корректность сортировки по имени клиента по убыванию.
    """)
    @pytest.mark.parametrize(
        "sort_order, expected_sorting",
        [
            ("ascending", False),
            ("descending", True),
        ],
    )
    def test_sort_customer_list(self, browser, sort_order, expected_sorting):
        page = CustomersListPage(browser)
        with allure.step("Открыть страницу со списком клиентов."):
            page.open(urls.CUSTOMERS_LIST)

        origin_list = tp.get_name_list(browser)

        if sort_order == "ascending":
            with allure.step("Сортировка списка клиентов по имени по возрастанию."):
                page.sort_btn_click()
                page.sort_btn_click()
        elif sort_order == "descending":
            with allure.step("Сортировка списка клиентов по имени по убыванию."):
                page.sort_btn_click()

        actual_list = tp.get_name_list(browser)
        expected_list = sorted(origin_list, reverse=expected_sorting)

        with allure.step(f"Проверка сортировки списка клиентов по имени по {sort_order}"):
            assert actual_list == expected_list, f"List is not sorted by {sort_order}"
