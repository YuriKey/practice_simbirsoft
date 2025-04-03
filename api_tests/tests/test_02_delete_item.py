from http import HTTPStatus

import allure
import requests

from api_tests.data.dataclasses.item_data import ItemData
from api_tests.data.urls import urls
from api_tests.utils.assertions import assertions as a


@allure.epic("Тестирование API.")
@allure.feature("Работа с сущностями.")
@allure.testcase("02_Удаление сущности.")
class TestDeleteItem:
    @allure.title("Удаление сущности по id.")
    @allure.description("""
        Тест проверяет:
        1. Получение данных сущности по id.
        2. Удаление созданной сущности.
        3. Отсутствие созданной сущности в списке всех сущностей.
        """)
    def test_delete_item(self, create_item):
        with allure.step("1. Создать сущность. Получить ее id."):
            item_id, _ = create_item

        with allure.step("2. Проверить, что созданная сущность существует."):
            response_before_delete = requests.get(f"{urls.BASE_URL}/get/{item_id}")
            a.assert_status_code(response_before_delete)
            ItemData(**response_before_delete.json())

        with allure.step("3. Отправить запрос на удаление созданной сущности."):
            delete_response = requests.delete(f"{urls.BASE_URL}/delete/{item_id}")
            a.assert_status_code(delete_response, HTTPStatus.NO_CONTENT)

        with allure.step("4. Проверить, что созданная сущность отсутствует."):
            response_after_delete = requests.get(f"{urls.BASE_URL}/get/{item_id}")
            a.assert_status_code(response_after_delete, HTTPStatus.INTERNAL_SERVER_ERROR)
