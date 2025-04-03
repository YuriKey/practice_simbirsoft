import allure
import requests

from api_tests.data.dataclasses.item_data import ItemData
from api_tests.data.urls import urls
from api_tests.utils.assertions import assertions as a


@allure.epic("Тестирование API.")
@allure.feature("Работа с сущностями.")
@allure.testcase("03_Получение всех сущностей.")
class TestGetAllItems:
    @allure.title("Получение всех сущностей с пагинацией.")
    @allure.description("""
        1. Создание сущности.
        2. Формирование страницы сущностей по параметрам пагинации.
        3. Статус код запроса на получение всех сущностей.
        4. Структуру каждой сущности.
        5. Ограничение пагинации.
    """)
    def test_get_all_items(self, create_item):
        with allure.step("1. Создать сущность и задать параметры пагинации."):
            _ = create_item
            params = {"page": 1, "perPage": 5}

        with allure.step("2. Отправить запрос с пагинацией."):
            response = requests.get(f"{urls.BASE_URL}/getAll/", params=params)
            response_data = response.json()
            items_list = response_data["entity"]

        with allure.step("3. Проверить статус код на получение всех сущностей."):
            a.assert_status_code(response)

        with allure.step("4. Валидировать структуру каждой сущности."):
            for item in items_list:
                ItemData(**item)

        with allure.step("5. Проверить ограничения пагинации."):
            assert 1 <= len(items_list) <= params["perPage"], (
                f"Количество сущностей вне диапазона. Ожидалось 1-5, получено {len(items_list)}."
            )
