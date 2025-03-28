import allure

from ui_tests.data.urls import Urls
from ui_tests.pages.customers_list_page import CustomersListPage
from ui_tests.utils import table_parser as tp, find_avg_name_length as fnl

urls = Urls()


@allure.story("Список клиентов")
@allure.testcase("AT02_Удаление клиента")
@allure.description("Проверка удаления клиента из таблицы по клику на кнопку Delete")
def test_avg_name_delete(browser):
    page = CustomersListPage(browser)
    with allure.step("Открыть страницу со списком клиентов"):
        page.open(urls.CUSTOMERS_LIST)

    origin_list = tp.get_name_list(browser)
    name = fnl.find_name_closest_to_average(origin_list)

    delete_btn_loc = page.get_delete_button_loc(name)

    with allure.step("Проверить наличие кнопки Delete на странице в строке выбранного клиента."):
        assert page.element_is_visible(delete_btn_loc)
        assert page.find_element(delete_btn_loc).text == "Delete"

    with allure.step("Нажать на кнопку Delete."):
        page.click(delete_btn_loc)
    updated_list = tp.get_name_list(browser)

    with allure.step("Проверить, что клиент не отображается в таблице."):
        assert name not in updated_list
