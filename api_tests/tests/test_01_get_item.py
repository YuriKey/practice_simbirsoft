from http import HTTPStatus

import allure
import requests

from api_tests.conftest import generator
from api_tests.data.dataclasses.item_data import ItemData
from api_tests.data.urls import urls
from api_tests.src.assertions import assertions as a


@allure.epic("Тестирование API.")
@allure.feature("Сущность.")
@allure.testcase("test_01_get_item")
@allure.title("Получение данных сущности по id.")
def test_get_item(create_item):
    with allure.step("Создать сущность. Получить ее id и данные."):
        item_id = create_item[0]
        expected_data = create_item[1]

    with allure.step("Получить данные сущности по id."):
        response = requests.get(f"{urls.BASE_URL}/get/{item_id}")

    with allure.step("Проверить статус код запроса на получение данных сущности."):
        a.assert_status_code(response)

    with allure.step("Сравнить полученные данные сущности с ожидаемыми."):
        a.assert_props(response, expected_data)


# # pydantic version
#
# @allure.epic("Тестирование API")
# @allure.feature("Сущность")
# @allure.testcase("test_00_create_item")
# @allure.title("Создание и проверка сущности")
# def test_create_item():
#     # 1. Генерация данных
#     data = generator.generate_item()
#
#     # 2. Отправка запроса
#     response = requests.post(f"{urls.BASE_URL}/create", json=data)
#     assert response.status_code == HTTPStatus.OK
#
#     # 3. Валидация ответа создания
#     created_item_id = response.json()
#
#     # 4. Получение и валидация данных
#     response = requests.get(f"{urls.BASE_URL}/get/{created_item_id}")
#     item = ItemData(**response.json())  # Валидация через Pydantic
#
#     # 5. Проверка значений
#     assert item.title == data["title"]
#     if data["addition"]:
#         assert item.addition.additional_info == data["addition"]["additional_info"]
#         assert item.addition.additional_number == data["addition"]["additional_number"]
#     assert item.important_numbers == data["important_numbers"]