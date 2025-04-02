from http import HTTPStatus

import allure
import requests

from api_tests.data.urls import urls
from api_tests.src.assertions import assertions as a


@allure.epic("Тестирование API.")
@allure.feature("Сущность.")
@allure.testcase("test_02_delete_item")
@allure.title("Удаление сущности по id.")
def test_delete_item(create_item):
    with allure.step("Создать сущность. Получить ее id."):
        item_id = create_item[0]

    with allure.step("Проверить, что созданная сущность существует."):
        response_before_delete = requests.get(f"{urls.BASE_URL}/get/{item_id}")
        a.assert_status_code(response_before_delete)

    with allure.step("Удалить созданную сущность."):
        requests.delete(f"{urls.BASE_URL}/delete/{item_id}")

    with allure.step("Проверить, что созданная сущность отсутствует."):
        response_after_delete = requests.get(f"{urls.BASE_URL}/get/{item_id}")
        a.assert_status_code(response_after_delete, HTTPStatus.INTERNAL_SERVER_ERROR)
