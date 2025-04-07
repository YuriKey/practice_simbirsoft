import allure
import requests

from api_tests.data.dataclasses.item_data import ItemData
from api_tests.data.urls import urls
from api_tests.utils.assertions import assertions as a


@allure.epic("Тестирование API.")
@allure.feature("Работа с сущностями.")
@allure.testcase("01_Получение данных сущности по id.")
@allure.title("Получение данных сущности.")
class TestGetItem:
    @allure.title("Получение данных сущности по id (positive case).")
    @allure.description("""
        Тест проверяет:
        1. Получение данных сущности по id.
        2. Идентичность полученных и переданных данных.
        """)
    def test_get_item(self, create_item):
        with allure.step("1. Создать сущность. Получить ее id и данные."):
            item_id, expected_data = create_item

        with allure.step("2. Получить данные сущности по id. Произвести валидацию через Pydantic."):
            response = requests.get(f"{urls.BASE_URL}/get/{item_id}")
            item = ItemData(**response.json())

        with allure.step("3. Проверить статус код запроса на получение данных сущности."):
            a.assert_status_code(response)

        with allure.step("4. Сравнить полученные данные сущности с ожидаемыми."):
            a.assert_props_are_equal(item, expected_data)
